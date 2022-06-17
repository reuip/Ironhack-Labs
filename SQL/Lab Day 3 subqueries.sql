USE sakila;
#1 How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT count(inventory_ID) as num_copies 
FROM inventory 
GROUP BY film_id 
HAVING film_id=(SELECT film_id FROM film WHERE title="Hunchback Impossible");

#2 List all films whose length is longer than the average of all the films.
SELECT title 
FROM film 
WHERE length>(SELECT avg(length) FROM film);

#3 Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name FROM actor WHERE actor_id in
(SELECT actor_id from film_actor WHERE film_id=
(SELECT film_id from film WHERE title="Alone Trip"));

/* #4 Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
Identify all movies categorized as family films. */

SELECT title FROM film WHERE film_id in
(SELECT film_id FROM film_category WHERE category_id in
(SELECT category_id FROM category WHERE name="Family"));

#Cleaner way to do it
SELECT title FROM film WHERE film_id in
(SELECT film_id FROM film_category
JOIN category USING (category_id)
WHERE name="Family");

/*5 Get name and email from customers from Canada using subqueries. 
Do the same with joins. Note that to create a join, 
you will have to identify the correct tables with their primary keys and foreign keys, 
that will help you get the relevant information. */

SELECT first_name,last_name,email from customer WHERE address_id in
(SELECT address_id FROM address WHERE city_id in 
(SELECT city_id FROM city WHERE country_id=
(SELECT country_id from country WHERE country="Canada")));


#6 Which are films starred by the most prolific actor? 
#Most prolific actor is defined as the actor that has acted in the most number of films. 
#First you will have to find the most prolific actor and then use that actor_id to find the different films that he/she starred.

SELECT title FROM film where film_id in
(SELECT film_id from film_actor where actor_id=
(SELECT actor_id from 
(SELECT actor_id,count(film_id) as num_films from film_actor GROUP BY actor_id ORDER BY num_films desc limit 1) temp));

#Cleaner way to do it from Rafa using WITH
WITH most_profilic_actor AS (select actor_id from film_actor
		group by actor_id order by count(film_id)desc limit 1)

SELECT title from film inner join film_actor using (film_id)
where actor_id = (select actor_id from most_profilic_actor);


#7 Films rented by most profitable customer. You can use the customer table and payment table to find the most profitable customer 
#ie the customer that has made the largest sum of payments

SELECT title from FILM WHERE film_id in  #inventory
(SELECT film_id FROM inventory WHERE inventory_id in  #was rented
(SELECT inventory_id FROM rental WHERE customer_id=  #fits the right customer
(SELECT customer_id from 
(SELECT customer_id, sum(amount) as total_paid FROM payment GROUP BY customer_id ORDER BY total_paid desc LIMIT 1) temp)));


#8 Customers who spent more than the average payments.
WITH customer_totals as (SELECT sum(amount) as amount_paid FROM payment GROUP BY customer_id)
SELECT first_name, last_name FROM customer WHERE customer_id in
(SELECT customer_id FROM
(SELECT customer_id, sum(amount) as total_payment FROM payment GROUP BY customer_id HAVING total_payment >
(SELECT avg(amount_paid) from customer_totals))temp) ORDER BY first_name;

#Cleaner way to do it
WITH customer_totals as (SELECT sum(amount) as amount_paid FROM payment GROUP BY customer_id)
SELECT first_name,last_name from customer 
JOIN payment USING (customer_id) GROUP BY customer_id 
HAVING sum(amount)>(SELECT avg(amount_paid) FROM customer_totals);
