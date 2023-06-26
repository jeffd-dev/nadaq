# Nadaq

Nadaq is a web application where users can share things with each other.

*It's like NASDAQ without the $*


## Status
⚠️ This project is actually a Proof of Concept with no stability and security warranty ⚠️

*Please wait for the version 1.0*


## Details

This self-hosted application try to stay as minimalist as possible: simple to deploy, simple to use, simple to customize and extend.

*To make life simpler for minimalists*

The primary goal is to provide an [ActivityPub](https://en.wikipedia.org/wiki/ActivityPub) tool for lending physical objects because it's a missing part of the ActivityPub ecosystem.


### Concepts

1. An user share items to a group of another users.
2. One user may have many groups, it allows to share one object with a specific group only (with a high trust level such as family members).
3. To borrow an item, user should contact the owner, there is no availability, reservation or stock managment. The project aims to help create social relation and keep this human step.
4. Application can be setup as permanent service or for a quick use (at an one-day event)

### Secondary Usages

The general idea is to share things (household appliances, DIY tools...) but application stay open to be used:
- as donation platform: for the exchange of seeds, plants, materials...
- as service platform: where the participants of an initiative can meet (such as the sharing of a personal compost)
- as human knowledge platform: were users can list their skills that they can teach to other community members
- as simple way to create web inventory from CSV file (books, board-games) with basic authentication


### Features in this POC

- create an user-group and add some users
- create item and share it with an user-group
- display available items for our user-groups
- join a public group


### Features planned

- create an account
- Item creation from CSV file
- ActivityPub support (as plugin)
- Item category
- Public user-group (Community) with an access code to join (for associations)
- Export as static-website
- Custom message for each form (privacy concern, best practices and conventions for new item...)
- French translation
- Email for lost password


## Usage

This alpha version comes with limited functionalities and **without any security**. This proof of concept is published to have a preview and help to find new functionnality or UX improvment.

### Installation

This Nadaq POC require Python 3.7+ and use SQLite database. 

The only dependency, [Bottle web framework](https://bottlepy.org), is included into a file to make virtualenv optional.

Then use the file `init_script.sql` to create a SQLite database inside the `db` folder.

```
sqlite3 ./db/database < ./db/init_script.sql
```

### Run

On MacOS/Linux: ```cd app; python3 nadaq.py```

The web application will be run at `localhost:8080`. You can login with: `demo/pwd` (but password is not checked).

## Contribute

### Code of conduct

Please read and follow the [code of conduct of the AFPY/PyconFr](https://www.pycon.fr/2023/en/conduct.html).

### Manifest of this project

- Simple (do one thing and do it well) with minimal dependencies
- Lightweight to run on limited hardware, lightweight interface to stay accessible to everyone
- [Secure](https://owasp.org/) with privacy warranty (personal data stored, can be run without internet access)
- Open to plug-in and customization

### Contributing welcome

This list is not exhaustive:
- Merge Request: code optimization, feature, tests, documentation, translation, etc
- Technical advices: security and privacy improvment, high availability features, best practices, etc
- Feedback: accessibility, functionnality idea, bugs, deployment improvments, etc

### Community

- Language: [EN] 🇬🇧 recommended, [FR] 🇨🇵 is understood
- Communication tool: *undefined*
- **Code style**: Python: PEP8 - CSS: *undefined* - JS: *undefined*
- Contact: Github or dev{@}zest-labs{.}fr (remove the `{}`)

## License

Nadaq is [MIT licensed](./LICENSE).

## Related Projects

*Here will be listed major forks, alternatives (application with the same goal in a different language) and other related projects*

### Low-Tech alternative

You can find a paperalternative on [this website](https://lesecolohumanistes.fr/lecologie-au-quotidien/pret-entre-voisins) [lang:fr]

