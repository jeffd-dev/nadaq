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
        <h2>User {{ user.name }}</h2>

        <p> <b>Member of:</b> 
        % for group in groups:
            <a href="/group/{{group.uid}}">{{ group.name }}</a>&nbsp; 
        % end
        </p>

        <ul class="action-list">
            <li>
                <a href="/create_relation/{{ user.uid }}">Add into group</a>
            </li>
        </ul>

        <p>Contact informations: {{ user.contact_info }}</p>

        <p>Location informations: {{ user.location_info }}</p>

    </div>

    
</body>
</html>