<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nadaq</title>
    <link rel="stylesheet" type="text/css" href="/static/neat.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
</head>

<body>
    <header>
        <h1>Nadaq</h1>
        <nav>
            <a href="/my_inventory">My inventory</a>
            <a href="/my_groups">Groups</a>
            <a href="/available_items">Available resources</a>
            <a href="/settings">Settings</a>
            <a href="/logoff">Logout from Jeffd</a>
        </nav>
    </header>

    <div class="main">
        <h2>Settings</h2>

        <p>Privacy warning: lorem ipsum dolor set nore dolor ipsum lorem</p>


        <form action="">

            <label for="contact">My contact informations:</label>
            <textarea id="contact" name="contact" name="story" rows="3" cols="42">{{ user.contact_info }}</textarea>

            <label for="location">My location:</label>
            <textarea id="location" name="location" name="story" rows="3" cols="42">{{ user.location_info }}</textarea>

            <button type="submit">Update</button>
        </form>
        
    </div>

    
</body>
</html>