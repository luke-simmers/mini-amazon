INSERT INTO Users VALUES
  (0, 'gogo@gmail.com', 'pbkdf2:sha256:150000$IbiV7iVE$065e657a4897d381b1595fc8e872d068ec1730a8d43e1a3921fedf85b50e4d70', 'Gogo', 'Gadget', '100 Downey Street'),
  (1, 'lugg@rzip.site', 'pbkdf2:sha256:150000$hTaPds9q$4d44bc1d03d6e6e709a73c51f7669f1eb7fe8b6a4374e3297f770b04f425f704', 'Pogo', 'Power', '102 Downey Street'),
  (2, 'uthedm2014t@iprloi.com', 'pbkdf2:sha256:150000$4nJGFmzT$639f74a1bf1de50fd8febd0789ace86da78455bd4d20614242e0f42b622e37c0', 'Togo', 'Toulousse', '104 Downey Street'),
  (3, '4eduardo.angel@21jag.com', 'pbkdf2:sha256:150000$kckJ71tP$0953e2a8aa536ca85e07710fc00bda9f23387e97f35ee9441658b5ade327f14c', 'Logo', 'Lowry', '106 Downey Street'),
  (4, 'dheshammazen627c@outlook.sbs', 'pbkdf2:sha256:150000$wgyF7GEV$4241b691fbb3eabc0bba8343aa715fff8cfd1dc0bce3beddce9ad81a6e7e9ce6', 'Shogo', 'Sheveries', '108 Downey Street');
  
INSERT INTO Sellers VALUES
  (0), (1), (2), (3), (4);
  
INSERT INTO Category VALUES
  ('Essentials'),
  ('Food'),
  ('Electronics'),
  ('Clothes'),
  ('Outdoor');
  
INSERT INTO Products VALUES
  (101, 0, 'Paper Towels', 'Abundantly Absorbent!', 'Essentials', '/static/images/paper_towel.jpg', 4.99, 5000),
  (102, 1, 'Kind Bars', 'All natural bars', 'Food', NULL, 5.99, 4000),
  (103, 2, 'Dyson Microwave', 'Mid service Microwave Oven', 'Electronics', NULL, 79.99, 32),
  (104, 3, 'Snowshoes', 'Perfect for hikes', 'Outdoor', NULL, 49.99, 8),
  (105, 4, 'Champion Hoodie', 'Decent hoodies and many colors', 'Clothes', NULL, 29.99, 55);

INSERT INTO OrderInformation VALUES
  (1001, 0, '2018-09-06 10:00:00'),
  (1002, 1, '2018-10-31 13:00:00'),
  (1003, 2, '2019-10-31 18:00:00'),
  (1004, 3, '2020-10-31 18:00:00'),
  (1005, 4, '2020-02-22 07:00:00');
  
INSERT INTO ItemsInOrder VALUES
  (1004, 101, 4, 4.99, 'Fulfilled'),
  (1003, 105, 2, 29.99, 'Not Fulfilled'),
  (1001, 102, 3, 5.99, 'Fulfilled'),
  (1005, 103, 31, 79.99, 'Fulfilled'),
  (1002, 104, 1, 49.99, 'Not Fulfilled');  
  
INSERT INTO ProductReview VALUES
  (0, 102, 4, 'Great! Love Kind Bars and the Cause!'),
  (2, 105, 2, 'Fell apart when I wore it'),
  (1, 104, 3, 'I was nearly eaten by a bear'),
  (4, 103, 5, 'Give me More Microwaves. I know there is one more. Give it to me'),
  (3, 101, 1, 'I am the type of person who would review paper towels on Amazon');   

INSERT INTO SellerReview VALUES
  (0,1,3,'Pretty Mediocre Seller'),
  (4,2,5,'Great. I get all my Microwave From this guy'),
  (1,3,1,'Poor quality product.'),
  (2,4,2,'Sells Poor Quality Merchandise, but very nice person.'),
  (3,0,4,'Reliable');
  
INSERT INTO CARTS VALUES
  (0,101,9,44.91),
  (4,104,5,249.95),
  (1,102,1,5.99),
  (2,105,3,89.97),
  (3,103,1,79.99);
