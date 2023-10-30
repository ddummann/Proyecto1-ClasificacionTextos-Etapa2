
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
                .no-border {
                    border: none !important;
                }
                .no-background {
                    background: none !important;
                    border: none !important;
                }


                .small-image {
                    width: 190px;
                    height: 190px;
                    border: none;
                }

                .align-card-right {
                    display: flex;
                    justify-content: flex-end;
                }

                .align-card-left {
                    display: flex;
                    justify-content: flex-start;
                }

                .align-card-center {
                    display: flex;
                    justify-content: center;
                }

                .flip-card {
                    background-color: transparent;
                    width: 190px;
                    height: 190px;
                    perspective: 1000px;
                    /* Remove this if you don't want the 3D effect */
                }

                /* This container is needed to position the front and back side */
                .flip-card-inner {
                    position: relative;
                    width: 190px;
                    height: 190px;
                    text-align: center;
                    transition: transform 0.8s;
                    transform-style: preserve-3d;
                }

                /* Do an horizontal flip when you move the mouse over the flip box container */
                .flip-card:hover .flip-card-inner {
                    transform: rotateY(180deg);
                }

                /* Position the front and back side */
                .flip-card-front,
                .flip-card-back,
                .flip-card-back-red,
                .flip-card-back-orange {
                    position: absolute;
                    width: 190px;
                    height: 190px;
                    -webkit-backface-visibility: hidden;
                    /* Safari */
                    backface-visibility: hidden;
                }

                /* Style the front side (fallback if image is missing) */
                .flip-card-front {
                    background-color: #bbb;
                    color: black;
                }

                /* Style the back side */
                .flip-card-back {
                    background-color: #4C9F38;
                    color: white;
                    transform: rotateY(180deg);
                }

                .flip-card-back-red {
                    background-color: #C5192D;
                    color: white;
                    transform: rotateY(180deg);
                }

                .flip-card-back-orange {
                    background-color: #FF3A21;
                    color: white;
                    transform: rotateY(180deg);
                }

                .centered-text {
                    font-size: 0.9em;
                    /* Adjust this value to make the font smaller or larger */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100%%;
                    margin: 0 20px;/
                }

            </style>
        </head>
        <body>
            <div class="blue-line"></div>
            <img src="https://raw.githubusercontent.com/Lina-go/PROYECTO_ECG/main/Imagenes/S_SDG_logo_without_UN_emblem_horizontal_Transparent_WEB.png"
             alt="Image Description" class="header-image">
            <div class="clear"></div>
            <center>
                <h1>API de Objetivos de Desarrollo Sostenible</h1>
    <style>
        .justificado {
            text-align: justify;
            max-width: 1000px;
            margin: 0 auto;
        }
        .centrado {
            text-align: center;
            max-width: 1000px;
            margin: 0 auto;
        }
    </style>
    </head>
    <body>
        <p class="justificado">Objetivos de Desarrollo Sostenible (ODS) son un conjunto de 17 metas globales establecidas por las Naciones Unidas en 2015, con el propósito de abordar los desafíos más apremiantes a los que se enfrenta la humanidad y el planeta. Estos objetivos abarcan áreas cruciales como la pobreza, el hambre, la salud, la educación, la igualdad de género, el agua limpia, el saneamiento, el trabajo decente, el crecimiento económico, y la acción climática, entre otros. El enfoque principal de los ODS es promover un desarrollo que sea sostenible en términos sociales, económicos y ambientales, buscando un equilibrio entre el crecimiento económico, el bienestar social y la protección del medio ambiente. La meta es lograr estos objetivos para el año 2030, fomentando la colaboración entre gobiernos, sector privado y sociedad civil, para construir un mundo más justo, inclusivo y sostenible. Cada objetivo se desglosa en metas específicas, y se proporcionan indicadores para medir los progresos realizados, asegurando así un seguimiento y evaluación constantes de los avances hacia el logro de estos objetivos universales.</p>
    </body>
    <br>
  
            </center>

            <div class="container">
                
                <div class="row">
                    <div class="col-md-2"></div> <!-- Empty space (1-2) -->

                    <div class="col-md-3 align-card-right">
                        <div class="flip-card">
                            <div class="flip-card-inner">
                                <div class="flip-card-front card-img-top small-image">
                                    <img class="card-img-top small-image"
                                        src="https://raw.githubusercontent.com/Lina-go/PROYECTO_ECG/main/Imagenes/S-WEB-Goal-03.png">
                                </div>
                                <div class="flip-card-back">
                                    <div class="centered-text">
                                        <p>Garantizar una vida sana y promover el bienestar de todos a todas las
                                            edades.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> <!-- Centered card 1 (3-6) -->

                    <div class="col-md-3 align-card-center">
                        <div class="flip-card">
                            <div class="flip-card-inner">
                                <div class="flip-card-front card-img-top small-image">
                                    <img class="card-img-top small-image"
                                        src="https://raw.githubusercontent.com/Lina-go/PROYECTO_ECG/main/Imagenes/S-WEB-Goal-04.png">
                                </div>
                                <div class="flip-card-back-red">
                                    <div class="centered-text">
                                        <p>Promover oportunidades de aprendizaje permanentes para todos.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> <!-- Centered card 2 (7-10) -->

                    <div class="col-md-3 align-card-left">
                        <div class="flip-card">
                            <div class="flip-card-inner">
                                <div class="flip-card-front card-img-top small-image">
                                    <img class="card-img-top small-image"
                                        src="https://raw.githubusercontent.com/Lina-go/PROYECTO_ECG/main/Imagenes/S-WEB-Goal-05.png">
                                </div>
                                <div class="flip-card-back-orange">
                                    <div class="centered-text">
                                        <p>Ir en contra los prejuicios y las asociaciones implícitas a menudo invisible para la igualdad
                                            de oportunidades.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> <!-- Centered card 2 (7-10) -->

                    <div class="col-md-2"></div> <!-- Empty space (11-12) -->
                </div>
            </div>



            <br><br>
            <center>                    
                <h3>Cargar Archivo de ODS</h3>

                <a id="go-back-link" href="/">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-left" viewBox="0 0 16 16">
                        <path d="M5.646 11.646a.5.5 0 0 1 0-.708L2.293 8l3.353-3.354a.5.5 0 0 1 .708.708L3.707 8l2.647 2.646a.5.5 0 0 1-.708.708z"/>
                        <path fill-rule="evenodd" d="M3.5 8a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 0 1h-8a.5.5 0 0 1-.5-.5z"/>
                    </svg>
                </a>
                <br>
                <p>
                    En esta API puedes ingresar un texto y te dirá a que objetivo de desarrollo sostenible pertenece.
                </p>
                <br>
                <div class="d-flex justify-content-center">
                    <form method="post" action="/predict-file" enctype="multipart/form-data" class="d-flex align-items-center">

                        <input type="file" name="file" id="file-input" class="custom-file-input" style="display: none;"
                            onchange="updateLabel()">
                        <label for="file-input" class="btn btn-outline-primary btn-sm m-0">Seleccionar archivo</label>
                        <div id="file-status" class="btn-sm m-0 ml-2">No file selected</div>

                        <button type="submit" class="btn btn-outline-primary btn-sm"
                            style="position: relative; top: -0px;">Clasificar</button>
                    </form>
                </div>

                
                <div class="row">
                    <div class="col-md-6 d-flex justify-content-end align-items-center">
                        <div id="plot1" style="margin-top: -49px;"></div>
                    </div>
                    

                    <div class="col-md-6 d-flex flex-column align-items-start">
                        <div class="card text-center no-border ml-0">

                            <div class="card-body mr-auto" id="plot2Card">
                                <div id="plot2"></div>
                            </div>
                            <div class="card-body mr-auto" id="plot3Card" style="display: none;">
                                <div id="plot3"></div>
                            </div>
                            <div class="card-body mr-auto" id="plot4Card" style="display: none;">
                                <div id="plot4"></div>
                            </div>

                            <div class="card-header no-background text-center">
                                <ul class="nav nav-pills card-header-pills justify-content-center" id="plotNav">
                                    <li class="nav-item">
                                        <a class="nav-link" href="#plot2Card">ODS 3</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link" href="#plot3Card">ODS 4</a>
                                    </li>
                                    <li class="nav-item">
                                        <a class="nav-link" href="#plot4Card">ODS 5</a>
                                    </li>
                                </ul>
                            </div>

                        </div>
                    </div>
                </div>
                <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
                <script>
                    var data1 = %s;
                    var data2 = %s;
                    var data3 = %s;
                    var data4 = %s;
                    Plotly.newPlot('plot1', data1);
                    Plotly.newPlot('plot2', data2);
                    Plotly.newPlot('plot3', data3);
                    Plotly.newPlot('plot4', data4);

                    // Add event listener for nav pills
                    document.getElementById('plotNav').addEventListener('click', function(e) {
                        if (e.target.tagName === 'A') {
                            // Hide all cards
                            document.getElementById('plot2Card').style.display = 'none';
                            document.getElementById('plot3Card').style.display = 'none';
                            document.getElementById('plot4Card').style.display = 'none';

                            // Show clicked card
                            document.querySelector(e.target.getAttribute('href')).style.display = 'block';

                            // Prevent default link behavior
                            e.preventDefault();
                        }
                    });
                </script>
                
                
                <div>
                    <a href="/download" download><button class="btn btn-outline-primary btn-sm">Descargar archivo</button></a>
                </div>
                <br><br>

                <h3>Escribir Texto</h3>
                <div>
                    <form method="get" action="/predict-text" id="textarea">
                        <textarea name="input" id="input" rows="4" cols="50" required></textarea>
                        <br><br>
                        <button type="submit" id="submit" class="btn btn-outline-primary btn-sm">Clasificar</button>
                    </form>
                </div>
            </center>
            <script>
                function updateLabel() {
                    const fileInput = document.getElementById("file-input");
                    const label = document.querySelector("label[for='file-input']");
                    const fileStatus = document.getElementById("file-status");

                    if (fileInput.files.length > 0) {
                        const fileName = fileInput.files[0].name;
                        fileStatus.innerText = fileName;
                    } else {
                        label.innerText = "Choose File";
                        fileStatus.innerText = "No file selected";
                    }
                }

            </script>
        </body>
    </html>
    """
