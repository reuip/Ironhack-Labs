Use sakila;
#1. Write a query to display for each store its store ID, city, and country.
SELECT store.store_id, city.city, country.country FROM store
JOIN address USING (address_id)
JOIN city USING (city_id)
JOIN country USING (country_id);

#2 Write a query to display how much business, in dollars, each store brought in.
SELECT store.store_id,sum(payment.amount)
FROM payment
JOIN staff using (staff_id)
JOIN store using (store_id)
GROUP BY store.store_id;

#3 What is the average running time(length) of films by category?
SELECT category.name, round(avg(film.length),2) as average_length FROM film
JOIN film_category using (film_id)
JOIN category using (category_id)
GROUP BY category.name;

#4 Which film categories are longest(length)? (Hint: You can rely on question 3 output.)
SELECT category.name, round(avg(film.length),2) as average_length FROM film
JOIN film_category using (film_id)
JOIN category using (category_id)
GROUP BY category.name
ORDER BY average_length desc;

#5 Display the most frequently(number of times) rented movies in descending order.
SELECT film.title FROM rental
JOIN inventory using (inventory_id)
JOIN film using (film_id)
GROUP BY film.film_id
ORDER BY count(rental.rental_id) desc;

#6 List the top five genres in gross revenue in descending order.
SELECT category.name, sum(payment.amount) as total_revenue
FROM payment
JOIN rental using (rental_id)
JOIN inventory using (inventory_id)
join film_category using (film_id)
join category using (category_id)
GROUP BY category.category_id
ORDER BY total_revenue desc
Limit 5;

#7 Is "Academy Dinosaur" available for rent from Store 1?
SELECT film.title, count(inventory.film_id) as "Copies Available" from film
JOIN inventory using (film_id)
JOIN store using (store_id)
WHERE (film.title="Academy Dinosaur" and store.store_id=1)
GROUP BY store.store_id;