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
        <h2>Share item `{{ item.name }}`</h2>

        % if item.information:
            <p>Description: {{ item.information }}</p>
        % end

        <form action="/item/{{item.uid}}/share" method="POST">
            <label for="group">Select an existing group:</label>
            <select name="group" id="group">
                <option value="0" selected="selected">Select a group</option>
                % for group in groups:
                    <option value="{{ group.uid }}"> {{ group.name }}</option>
                % end
            </select>

            <label for constraint>Constraint:</label>
            <input type="text" name="constraint" id="constraint">

            <button type="submit">Share item with this group</button>
        </form>
        
    </div>
</body>
</html>