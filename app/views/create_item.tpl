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
        <h2>Create new item</h2>

        <form action="/create_item" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">

            <label for="informations">Informations</label>
            <input type="text" id="informations" name="informations">

            <label for="constraint">Constraint</label>
            <input type="text" id="constraint" name="constraint">

            <label for="category">Category</label>

            <select id="category" name="category">
                % for category in categories:
                    <option value="{{ category }}">{{ category }}</option>
                % end
            </select>

            <button type="submit">Create</button>
        </form>
        
    </div>

    
</body>
</html>