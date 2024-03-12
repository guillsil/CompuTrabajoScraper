import scrapy


class ComputrabajoSpider(scrapy.Spider):
    name = "compuTrabajo"
    allowed_domains = ["ar.computrabajo.com"]
    start_page = 1  # Página inicial
    max_pages = 10  # Límite de páginas

    # Definir los valores de los parámetros
    localizacion = "capital-federal"
    orden = "publicationtime"
    empleo = ""

    # Construir la URL inicial basada en los parámetros
    if empleo is "":
        if start_page == 1:
            start_urls = [f"https://ar.computrabajo.com/empleos-en-{localizacion}?by={orden}"]
        else:
            start_urls = [f"https://ar.computrabajo.com/empleos-en-{localizacion}?by={orden}&page={start_page}"]
    else:
        if start_page == 1:
            start_urls = [f"https://ar.computrabajo.com/trabajo-de-{empleo}-empleos-en-{localizacion}?by={orden}"]
        else:
            start_urls = [f"https://ar.computrabajo.com/trabajo-de-{empleo}-empleos-en-{localizacion}?by={orden}&page={start_page}"]

    def parse(self, response):
        ofertas = response.css("article.box_offer")
        for oferta in ofertas:
            link_id = oferta.css("h2.fs18 a::attr(href)").get().strip()
            empresa = oferta.css("p.fs16 a::text").get()
            if not empresa:  # Si no se encuentra dentro de <p>, buscar en el texto circundante
                empresa = oferta.css("p.fs16::text").get().strip()
            else:
                empresa = empresa.strip()

            yield {
                "trabajo_nombre": oferta.css("h2.fs18 a::text").get().strip(),
                "empresa": empresa,
                "lugar_trabajo": oferta.css("p.fs16 span::text").get().strip(),
                "tipo_empleo": oferta.css("p.fs13.fc_aux::text").get().strip(),
                "link_empleo": f"https://ar.computrabajo.com{link_id}",
            }

        # Obtener el enlace a la siguiente página
        next_page_url = response.css("span.b_primary.w48.buildLink.cp::attr(data-path)").get()
        if next_page_url and self.start_page < self.max_pages:
            yield scrapy.Request(next_page_url, callback=self.parse)

        self.start_page += 1
