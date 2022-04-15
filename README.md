# Social-Network-API
This is an API Built in Django Rest Framework for a Social Network such as Twitter.

## Planning
**Question:** _Write down questions you have for the Product Manager about implementation._
- Why do we need to have this feature isolated in the User Profile Page? Sounds natural to me to see posts and comments on the homepage.
    - What do you think of having this feature on the homepage instead? Or why not on the homepage?
- Does this page show other users' replies exclusively to my posts? or does it show my replies in other users' posts?
- What about User Permissions? Would repliers be able to see other users' replies too?
- Can unfollowed users reply to any post?

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
    - I would use AWS and use it at the beginning either Vertical or Horizontal Scaling. Usually, Horizontal Scaling is the best, but I would evaluate both.
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
