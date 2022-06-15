Use sakila;
#1. Which actor has appeared in the most films?
SELECT a.first_name, a.last_name, count(b.film_id) as num_appearances
FROM actor a 
JOIN film_actor b 
USING (actor_id)
GROUP BY a.actor_id, a.first_name, a.last_name
ORDER BY num_appearances desc
LIMIT 1;

#2. Most active customer (the customer that has rented the most number of films)
SELECT a.first_name, a.last_name, count(b.rental_id) as num_rentals
FROM customer a 
JOIN rental b 
USING (customer_id)
GROUP BY a.customer_id, a.last_name, a.first_name
ORDER BY num_rentals desc
LIMIT 1;

#3. List number of films per category.
SELECT a.name, count(b.film_id) as num_films
FROM category a 
JOIN film_category b 
USING (category_id)
GROUP BY b.category_id
ORDER BY num_films;

#4. Display the first and last names, as well as the address, of each staff member.
SELECT a.first_name, a.last_name, b.address
FROM staff a 
JOIN address b 
USING (address_id);

#5. Display the total amount rung up by each staff member in August of 2005.
SELECT a.first_name, a.last_name, sum(b.amount) as total_amt
FROM staff a 
JOIN payment b 
USING (staff_id)
WHERE b.payment_date between "2005-08-01" and "2005-08-31"
#WHERE year(payment_date)=2005 and month(payment_date)=08
GROUP BY staff_id;

#6. List each film and the number of actors who are listed for that film.
SELECT a.title, count(b.actor_id) as num_actors
FROM film a
LEFT JOIN film_actor b
USING (film_id)
GROUP BY a.film_id, a.title
ORDER BY num_actors desc;

/*7. Using the tables payment and customer and the JOIN command, list the total paid by each customer. 
List the customers alphabetically by last name.
 */
SELECT customer.first_name, customer.last_name, sum(payment.amount) as total_paid
FROM customer
JOIN payment
USING (customer_id)
GROUP BY payment.customer_id
ORDER BY customer.last_name;

# Optional: Which is the most rented film? The answer is Bucket Brotherhood 
# This query might require using more than one join statement. Give it a try.

# rental - inventory (inv ID) - film name (film ID) - 
SELECT film.title, count(rental.rental_id) as count_mov FROM rental
JOIN inventory using (inventory_id)
JOIN film using (film_id)
GROUP BY film.film_id
ORDER BY count_mov desc
LIMIT 1;