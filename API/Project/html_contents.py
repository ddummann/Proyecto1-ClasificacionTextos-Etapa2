
def html_content_pie_graph():
    return """
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            <link rel="icon" href="https://www.ilo.org/wcmsp5/groups/public/---ed_emp/documents/image/wcms_625841.png"
            type="image/x-icon">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500;900&display=swap" rel="stylesheet">


            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
            crossorigin="anonymous"></script>

            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
            
            <style>
                head {
                    font-family: "Open Sans", sans-serif;
                }
                body {
                    font-family: 'Roboto', sans-serif;
                    text-align: center;
                    /* Reemplazo para <center> */
                }
                .btn-custom {
                font-size: 12px;
                border: 1px solid #656565;
                background-color: #EFEFEF;
                border-radius: 2.5px;
                }
                .clear {
                    clear: left;
                }
                .btn-seleccion {
                    font-size: 12px;
                }
                .btn-custom:hover {
                    background-color: ;
                }
                .btn-custom:focus {
                    outline: none;
                    background-color: #EFEFEF;
                }
                .btn-sm {
                    padding: 0.25rem 0.5rem;
                    font-size: 12px;
                }
                .header-image {
                    float: left;
                    margin-right: 200px;
                    height: auto;
                    width: 600px;
                    margin-top: 15px;
                }
                .blue-line {
                    background-color: #009DDA;
                    height: 5px;
                    top: 0;
                    left: 0;
                    
                }
            </style>
        </head>
        <body>
            <div class="blue-line"></div>
            <img src="https://raw.githubusercontent.com/Lina-go/PROYECTO_ECG/main/Imagenes/S_SDG_logo_without_UN_emblem_horizontal_Transparent_WEB.png"
             alt="Image Description" class="header-image">
            <div class="clear"></div>
            <center>
                <h1>
                    API de Objetivos de Desarrollo Sostenible
                </h1>
                <h2>
                    Objetivos de Desarrollo Sostenible
                </h2>
                <p>
                    En esta API puedes ingresar un texto y te dirá a que objetivo de desarrollo sostenible pertenece.
                </p>
            </center>
            <br>
            <center>                    
                <h3>Cargar Archivo de ODS</h3>
                <div>
                    <form method="post" action="/predict-file" enctype="multipart/form-data">
                        <input type="file" name="file" class="btn-seleccion">
                        <button type="submit" class="btn-custom">Clasificar</button>
                    </form>
                </div>
                <div id="plot"></div>
                <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
                <script>
                    var data = %s;
                    Plotly.newPlot('plot', data);
                </script>
                <div>
                    <a href="/download" download><button class="btn-custom">Descargar archivo</button></a>
                </div>
                <br><br>
                <h2>Escribir Review</h2>
                <div>
                    <form method="get" action="/predict-text" id="textarea">
                        <textarea name="input" id="input" rows="4" cols="50" required></textarea>
                        <br><br>
                        <button type="submit" id="submit" class="btn-custom">Clasificar</button>
                    </form>
                </div>
            </center>
        </body>
    </html>
    """
