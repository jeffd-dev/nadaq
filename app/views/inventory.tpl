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
        <h2>Available resources</h2>

        <p>
        <b>Filter by category:</b>
        % for category in categories:
            <a href="/available_items/filter/{{category}}">{{category}}</a>
        %end
        </p>


        <div class="list">
            % for item in item_list:
                <div class="inventory-item">
                    <span class="name">{{ item.name }}</span>
                    <span class="category">{{ item.category }}</span>
                    <a href="/item/{{ item.uid }}">Details</a>
                </div>
            % end
        </div>
    </div>

</body>
</html>