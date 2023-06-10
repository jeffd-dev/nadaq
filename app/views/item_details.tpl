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
        <h2>Item `{{ item.name }}`</h2>

        % if item.information:
            <p><b>Information</b>: {{ item.information }}</p>
        % end

        % if item.category:
            <p><b>Category</b>: {{ item.category }}</p>
        % end

        % if item.constraint:
            <p><b>Constraint</b>: {{ item.constraint }}</p>
        % end

        % if item_owner:
            <h3>Contact</h3>
            Please contact: {{ item_owner.name }}
            <ul>
            <li>{{ item_owner.contact_info }}</li>
            <li>{{ item_owner.location_info }}</li>
            </ul>
        % end


        <h3> Shared with </h3>
        <ul>
            % for group in shared_groups:
                <li><a href="/group/{{ group.uid }}">{{ group.name}}}</a></li>
            % end
        </ul>

    </div>

    
</body>
</html>