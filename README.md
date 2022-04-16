# Social-Network-API: Geovane Pacheco da Rocha
This is an API Built-in Django Rest Framework using the latest Django version (4.0) for a Social Network such as Twitter. This is also part of the _Strider_ hiring process where an API for two pages must be built in 7 days. In my case, due to the work, I had less time, but I was able to implement almost everything with some cool bonus features.

I am going present what was done now. For questions, critiques, or compliments, please send me an email: geovane.pacheco99@gmail.com.

## What was done
Besides the Bonus section, here is what was done on each of the above two pages: _User Profile_ and _Homepage_.

### Bonus
#### Database documention and schema
I do like to document everything, and it is also a good starting point. Because of that, the first thing I did was to build this Database Diagram to understand mode about the project scope, entities, and their relationships.

I decided to keep it simple and small using the Many-to-Many relationship as represented in the following image:
<p align="center">
    <img width="487" alt="image" src="https://user-images.githubusercontent.com/3878792/163651242-764d0c8e-048f-4885-94b8-427eea3a1140.png">
</p>

#### Docker and Docker-compose
I have used Docker and Docker-compose as a Mega Bonus approach since one of the biggest bottlenecks of every company is having engineers wasting too much time configuring their local setups/pushing code to production.

Having the whole structure built over Docker is a crucial requirement of any project.

#### Login and Permission Rules
The whole Login and Authorization feature was implemented and it can be verified through the login API: 
http://localhost:8000/api/login/

With that, I was able to create permissions rules that **deny** non-authenticated users to:
- Update other Users.
- Delete other Users.
- Create Posts.
- Update Posts.
- Delete Posts.

Here is an example of Authentication and Permissions being applied successfully in a non-logged user.
<p align="center">
    <img width="1790" alt="image" src="https://user-images.githubusercontent.com/3878792/163651973-102cb853-4019-4b84-b330-c232b55937f6.png">
</p>


### User Profile
On this page, the User can:
- See all users and then enable him to see who he can follow. (Bonus)
- Filter/Search and Sort all these Users. (Bonus)
- Insert a new user. (Bonus)
- See detailed user information through the api, example: `api/userprofile/2/`.
- On his user, he can Follow/Unfollow users during his account update.

Besides that, validators were also created to meet the requirements.

### Homepage
On this page, the User can:
- See all posts paginated by every 10 posts and sorted by the newest first.
- Create new posts.
- Filter/Search posts and repost. (Bonus)

Besides that, validators were also created to meet the requirements.

## Recorded videos
- Login/Authentication: https://recordit.co/XembFsQxUp
- Permissions: https://recordit.co/yOvp0ecSUq
- Creating/Updating and Deleting a User: https://recordit.co/KNBmQnAYYn
- Validators: https://recordit.co/SX6JCIHseD
- Creating a Post/RePost: https://recordit.co/zwOxGC4nEG

## Planning
**Question:** _Write down questions you have for the Product Manager about implementation._
- Why do we need to have this feature isolated in the User Profile Page? Sounds natural to me to see posts and comments on the homepage.
    - What do you think of having this feature on the homepage instead? Or why not on the homepage?
- Does this page show other users' replies exclusively to my posts? or does it show my replies in other users' posts?
- What about User Permissions? Would repliers be able to see other users' replies too?
- Can unfollowed users reply to any post?
- Probably no, but can non-logged users reply to posts? Maybe as anonymous?

**How I would solve:**
- I would first adapt the documentation and diagrams to update this new change.
    - For example, now the post entity would also have an interaction with a reply table, where a post can have several replies, but every reply belongs to one post.
    - It would also need to have a reference to the User where a User can make several replies and each reply belongs to one User.
- The API would need to be updated depending on the Feature Criteria, but I imagine User and Post Permissions would also need to be updated.
- New endpoints would need to be created regarding the "Reply Post" feature.
    - Another endpoint could be to search Users (maybe following users) and their posts to enable the "mentioning" feature.


## Critique
**Question:** _Reflect on this project, and write what you would improve if you had more time._
1. I would implement the remaining features such as:
     - Toggle button to show posts of All/Following users.
     - User's 5 posts per day limitation
2. I would definitely have created more automated tests.
3. Replaced my original bonus search by an advanced search engine.

### Critique - Scaling
**Question:** _If this project were to grow and have many users and posts, which parts do you think would fail first?_ <br />
**Answer:** The Homepage would be overloaded with the current number of posts/reposts and it could get even worse with the "Reply Post" feature.

**Question:** _In a real-life situation, what steps would you take to scale this product?_ <br />
**Answer:** I am going to split this answer into different steps:
1. Project and Code analysis.
    - Sometimes, bad code can be introduced causing bottlenecks and system overload.
2. Infrastructure Upgrade
    - I would use AWS. In the beginning, I would analyze and use either Vertical or Horizontal Scaling. Usually, Horizontal Scaling is the best, but I would evaluate both.
    - Define Auto Scaling Groups and Load Balancer to the project.
3. Postgres Database indexing.
4. For reposts and also the possibility to have the "Reply Post" feature, using the Django `prefetch_related` would help a lot.
5. Django also has a Cache Framework that could also be used.
6. Elasticsearch could also be used in heavy searches.

**Question:** _What other types of technology and infrastructure might you need to use?_ <br />
**Answer:**
<br />
- For Technology: Django and Django Rest Framework in the Backend to build the server and APIs. ReactJS with CSS3/SASS in the Frontend. For the Database I would avoid SQLite as much as possible, so that is why I started using Postgres.
- For Infrastructure: Amazon Web Service (AWS) would definitely be my choice for infrastructure. Besides that, having Docker and Docker Compose is something that I always start any project using it. Finally, having CI (Continuous Integration) enabled would help a lot.

## Instructions to execute it locally
This project uses Docker (version 20.10.13) and Docker compose (version 2.3.3), so, due to that, the local execution is pretty easy.

Just execute:
```
docker compose -f docker-compose.development.yml up --build
```

As any Django Project, make sure to prepare your Database in the first execution also running the migrations in the `web` docker container:
```
docker compose -f docker-compose.development.yml exec web bash
python manage.py makemigrations posterr_api
python manage.py migrate
```

_Sometimes you can get some port conflicts with the DB during the first initialization, feel free to try again later._

### How to execute tests
```
docker compose -f docker-compose.development.yml exec web bash
./manage.py test
```
