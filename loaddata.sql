CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
  -- FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
);

DROP TABLE IF EXISTS "Posts";


CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');



<<<<<<< HEAD

INSERT INTO `Posts` VALUES (null, 1, "The Future of AI", "2024-11-01", "https://example.com/image1.jpg", "A deep dive into the future advancements of artificial intelligence.", 1);
INSERT INTO `Posts` VALUES (null, 2, "Top 10 Healthy Foods", "2024-10-30", "https://example.com/image2.jpg", "An article discussing the top 10 healthiest foods to incorporate into your diet.", 1);
INSERT INTO `Posts` VALUES (null, 3, "Minimalism: The Art of Less", "2024-10-28", "https://example.com/image3.jpg", "How adopting minimalism can lead to a simpler, happier life.", 1);
INSERT INTO `Posts` VALUES (null, 4, "The Rise of Women's Football", "2024-10-25", "https://example.com/image4.jpg", "A look at how women's football is gaining global popularity.", 1);
INSERT INTO `Posts` VALUES (null, 5, "Top 5 Budget-Friendly Destinations", "2024-10-20", "https://example.com/image5.jpg", "Exploring the best travel destinations for those on a budget.", 0);
INSERT INTO `Posts` VALUES (null, 6, "Vegan Recipes for Beginners", "2024-10-15", "https://example.com/image6.jpg", "A collection of simple and delicious vegan recipes to get started.", 1);
INSERT INTO `Posts` VALUES (null, 7, "The Impact of 5G on Connectivity", "2024-10-10", "https://example.com/image7.jpg", "Exploring how 5G will revolutionize mobile connectivity around the world.", 1);
INSERT INTO `Posts` VALUES (null, 8, "Yoga for Stress Relief", "2024-10-05", "https://example.com/image8.jpg", "How yoga can help alleviate stress and improve mental well-being.", 1);
INSERT INTO `Posts` VALUES (null, 9, "The Benefits of Journaling", "2024-10-01", "https://example.com/image9.jpg", "Why journaling can improve mental clarity and help you achieve your goals.", 0);
INSERT INTO `Posts` VALUES (null, 10, "The Evolution of Extreme Sports", "2024-09-28", "https://example.com/image10.jpg", "A history of extreme sports and their growing popularity.", 1);
INSERT INTO `Posts` VALUES (null, 11, "Solo Travel Tips for First-Timers", "2024-09-22", "https://example.com/image11.jpg", "Advice for solo travelers looking to explore the world on their own.", 1);
INSERT INTO `Posts` VALUES (null, 12, "How to Make the Perfect Coffee", "2024-09-20", "https://example.com/image12.jpg", "A guide to brewing the perfect cup of coffee every time.", 1);
INSERT INTO `Posts` VALUES (null, 13, "Blockchain Beyond Cryptocurrency", "2024-09-18", "https://example.com/image13.jpg", "Exploring how blockchain technology is impacting industries beyond just finance.", 0);
INSERT INTO `Posts` VALUES (null, 14, "Mental Health in the Workplace", "2024-09-15", "https://example.com/image14.jpg", "How employers can create a healthy mental environment for their employees.", 1);
INSERT INTO `Posts` VALUES (null, 15, "Building a Successful Morning Routine", "2024-09-12", "https://example.com/image15.jpg", "How to structure your mornings for maximum productivity and focus.", 1);

INSERT INTO `Posts` VALUES (null, 1, "The Evolution of Jazz", "2024-11-01", "https://example.com/image1.jpg", "A deep dive into the history and impact of jazz music.", 1);
INSERT INTO `Posts` VALUES (null, 2, "Top 10 Must-Read Novels of the Decade", "2024-10-30", "https://example.com/image2.jpg", "A list of the best novels from the past ten years that every book lover should read.", 1);
INSERT INTO `Posts` VALUES (null, 3, "The Rise of Indie Music", "2024-10-28", "https://example.com/image3.jpg", "How independent artists are shaping the modern music scene.", 1);
INSERT INTO `Posts` VALUES (null, 4, "Understanding Classical Music", "2024-10-25", "https://example.com/image4.jpg", "A guide to appreciating the beauty and complexity of classical music.", 1);
INSERT INTO `Posts` VALUES (null, 5, "Books That Will Change Your Life", "2024-10-20", "https://example.com/image5.jpg", "A selection of books that have had a profound impact on readers around the world.", 0);

DELETE FROM `Posts` WHERE `id` IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15);



SELECT
    a.id,
    a.title
FROM posts a

SELECT * FROM posts;
=======
SELECT
    a.id,
    a.follower_id,
    a.author_id,
    a.created_on
FROM Subscriptions a

SELECT
            a.id,
            a.author_id,
            a.post_id,
            a.content
        FROM Comments a
>>>>>>> 2e62a6942131c63217eb62ec60236b5a4bd4c622
