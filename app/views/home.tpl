<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="icon" href="/static/favicon-32.png"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nadaq</title>
    <link rel="stylesheet" type="text/css" href="/static/neat.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
</head>

<body>
    <header>
        <h1>Nadaq</h1>
    </header>

    <div class="main">
        % if message:
            <div class="row home-message">
                {{ message }}
            </div>
        % end

        <div class="row">
            <div class="column">
                <ul class="action-list">
                    <li><a href="">Discover Nadaq with demo account</a></li>
                    <li><a href="">Create an account</a></li>
                </ul>

            </div>
    
            <div class="column">
                <p>Already have an account:</p>
                <form id="connection-form" action="/login" method="post">
                    <label for="login">Login:</label>
                    <input type="text" name="login" id="login" required>

                    <label for="password">Password:</label>
                    <input type="password" name="password" id="password" required>
                    <button type="submit">Connection</button>
                </form>
            </div>
        </div>

        <article>
            <h2>Welcome on Nadaq</h2>
            <p>This tools allow you to list your resources and share them with the other users.</p>

            <p>This instance is owned by ~Instance Owner~ - Contact is: blabla@nadaq.org </p>

            <p>Lorem ipsum dolor ... --instance description-- </p>

            <p>See our <a href="">Code of conduct</a> and our <a href="">Privacy policy</a>.</p>
        </article>

    </div>

    
</body>
</html>