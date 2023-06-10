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
        <h2>Groups</h2>

        <ul class="action-list">
            <li>
                <a href="/create_group">Create new group</a>
            </li>
        </ul>

        <h3> My groups </h3>

        <div class="list">
            % for group in groups:
                <div class="group-item">
                    <span class="name"> {{ group.name }} </b></span>
                    % if group.informations:
                       - <span class="details">{{ group.informations }}</span>
                    % end

                    <a title="See users in this group" href="/group/{{ group.uid }}">[ See members]</a>

                    % if group.is_public:
                        - (public group)
                    % else:
                        - <a href="">Edit</a>
                    % end
                </div>
            % end
        </div>

        <h4>You are member of the following groups</h4>
        <ul>
            % for member_group in member_groups:
                <li><a href="/group/{{ member_group.uid }}">{{ member_group.name}}</a></li>
            % end
        </ul>

    </div>
</body>
</html>