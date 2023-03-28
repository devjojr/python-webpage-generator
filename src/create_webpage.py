def create_html(name):
    html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>HTML Template</title>
            <link rel="stylesheet" href="style.css" />
            <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
            />
        </head>
        <body>
            <header class="grid">
            <h1>My Site</h1>
            <nav>
                <a href="http://"><strong>Home</strong></a>
                <a href="http://"><strong>Contact</strong></a>
            </nav>
            </header>
            <main class="grid">
            <div class="my-site">
                <h2>Lorem Ipsum</h2>
                <p>
                Dolor sit amet consectetur, adipisicing elit. Asperiores nemo tempore
                eum velit, aliquam quaerat harum impedit quibusdam architecto tempora
                doloremque! Ullam, aliquam! Porro quos distinctio magni dolores,
                eligendi suscipit.
                </p>
            </div>
            <img src="http://via.placeholder.com/700x400" alt="insert your image" />
            </main>
            <section class="grid">
            <h2>What We Do</h2>
            <div class="card">
                <h3>Excepteur</h3>
                <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur,
                alias dicta? Deserunt odio corporis nemo a dolor voluptate aperiam
                neque. Quas qui repudiandae voluptatibus fugiat quam velit dignissimos
                quod aliquid.
                </p>
            </div>
            <div class="card">
                <h3>Occaecat</h3>
                <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur,
                alias dicta? Deserunt odio corporis nemo a dolor voluptate aperiam
                neque. Quas qui repudiandae voluptatibus fugiat quam velit dignissimos
                quod aliquid.
                </p>
            </div>
            <div class="card">
                <h3>Upidatat</h3>
                <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur,
                alias dicta? Deserunt odio corporis nemo a dolor voluptate aperiam
                neque. Quas qui repudiandae voluptatibus fugiat quam velit dignissimos
                quod aliquid.
                </p>
            </div>
            </section>
            <section class="grid">
            <h2>About Us</h2>
            <div class="about-card">
                <img
                src="http://via.placeholder.com/500x333"
                alt="Ellie Williams"
                style="width: 100%"
                />
                <h1>Ellie Williams</h1>
                <p class="title">Founder & CEO</p>
                <p>FEDRA University</p>
                <div>
                <a href="#"><i class="fa fa-twitter"></i></a>
                <a href="#"
                    ><i class="fa fa-linkedin" style="margin-left: 10px"></i
                ></a>
                <a href="#"
                    ><i class="fa fa-facebook" style="margin-left: 10px"></i
                ></a>
                </div>
            </div>
            <div class="about-card">
                <img
                src="http://via.placeholder.com/500x333"
                alt="Din Djarin"
                style="width: 100%"
                />
                <h1>Din Djarin</h1>
                <p class="title">COO</p>
                <p>Mud Horn University</p>
                <div>
                <a href="#"><i class="fa fa-twitter"></i></a>
                <a href="#"
                    ><i class="fa fa-linkedin" style="margin-left: 10px"></i
                ></a>
                <a href="#"
                    ><i class="fa fa-facebook" style="margin-left: 10px"></i
                ></a>
                </div>
            </div>
            <div class="about-card">
                <img
                src="http://via.placeholder.com/500x333"
                alt="Ganon Dorf"
                style="width: 100%"
                />
                <h1>Ganon Dorf</h1>
                <p class="title">CFO</p>
                <p>Hyrule University</p>
                <div>
                <a href="#"><i class="fa fa-twitter"></i></a>
                <a href="#"
                    ><i class="fa fa-linkedin" style="margin-left: 10px"></i
                ></a>
                <a href="#"
                    ><i class="fa fa-facebook" style="margin-left: 10px"></i
                ></a>
                </div>
            </div>
            <div class="about-card">
                <img
                src="http://via.placeholder.com/500x333"
                alt="Homer Simpson"
                style="width: 100%"
                />
                <h1>Homer Simpson</h1>
                <p class="title">Director</p>
                <p>Springfield University</p>
                <div>
                <a href="#"><i class="fa fa-twitter"></i></a>
                <a href="#"
                    ><i class="fa fa-linkedin" style="margin-left: 10px"></i
                ></a>
                <a href="#"
                    ><i class="fa fa-facebook" style="margin-left: 10px"></i
                ></a>
                </div>
            </div>
            </section>
            <footer class="grid">
            <div class="contact">
                <h2>Contact Us</h2>
            </div>
            <div class="contact-info">
                <div class="contact-address">
                <p>742 Evergreen Terrace</p>
                <p>Springfield, CA 90210</p>
                <p>(123) 456-7890</p>
                <p>mybusiness@test.com</p>
                <div class="address-link">
                    <a href="#"><i class="fa fa-twitter address-fa"></i></a>
                    <a href="#"
                    ><i
                        class="fa fa-instagram address-fa"
                        style="margin-left: 10px"
                    ></i
                    ></a>
                    <a href="#"
                    ><i
                        class="fa fa-facebook address-fa"
                        style="margin-left: 10px"
                    ></i
                    ></a>
                </div>
                </div>
            </div>
            </footer>
        </body>
        </html>
    """
    return html


def create_css():
    css = """
        @import url("https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,wght@0,200;0,300;0,400;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,600;1,700;1,800;1,900&display=swap");

        body {
            margin: 0;
            font-family: "Nunito Sans";
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: 30px;
        }

        header {
            padding: 0px 50px;
            align-items: center;
        }

        header h1 {
            grid-column: span 6;
        }

        header nav {
            grid-column: span 6;
            justify-self: end;
        }

        header nav a {
            color: #333;
            margin-left: 10px;
            text-decoration: none;
        }

        main,
        section {
            max-width: 1200px;
            margin: 60px auto;
            padding: 20px;
        }

        main .my-site {
            grid-column: span 5;
        }

        main img {
            grid-column: 7 / span 6;
            width: 100%;
            border-radius: 5px;
        }

        section > h2 {
            grid-column: span 12;
            text-align: center;
            font-size: 1.5em;
            padding-top: 20px;
        }

        section .card {
            grid-column: span 4;
            background: white;
            padding: 10px 20px;
            border-radius: 10px;
            box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
        }

        section .about-card {
            grid-column: span 3;
            background: white;
            padding-bottom: 10px;
            box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
            text-align: center;
        }

        section .about-card a {
            color: hsl(204, 86%, 53%);
            font-size: 1.2em;
        }

        footer > .contact {
            grid-column: span 12;
            text-align: center;
            padding-top: 10px;
            background: hsl(0, 0%, 71%);
            margin-bottom: -30px;
        }

        footer > .contact-info {
            grid-column: span 12;
            text-align: center;
            padding-top: 10px;
            background: hsl(0, 0%, 29%);
        }

        footer > .contact-address {
            justify-self: end;
        }

        footer .contact-address,
        .address-fa {
            color: white;
        }

        footer p {
            margin: auto;
        }

        footer .address-link {
            margin: 10px 0 10px 0;
        }

        footer .address-fa {
            font-size: 1.2em;
        }

        @media screen and (max-width: 960px) {

            main img {
                grid-column: 2 / span 10;
            }

            main .my-site {
                grid-column: 3 / span 8;
                text-align: center;
            }

            section .card {
                grid-column: 3 / span 8;
            }

            section .about-card {
                grid-column: 3 / span 8;
            }
        }
    """
    return css


name = "HTML Template"
html = create_html(name)
css = create_css()

with open('index.html', 'w') as f:
    f.write(html)

with open('style.css', 'w') as f:
    f.write(css)
