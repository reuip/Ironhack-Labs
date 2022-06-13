USE sakila;
# Review tables in the database
show tables;

#Explore tables by selecting all columns in them
SELECT * FROM actor;
SELECT * FROM address;
SELECT * FROM film;

#Select one column. Get film titles
SELECT title FROM film;

#Select one column from a table and alias it. 

SELECT sum(amount) as "Total Owed" FROM payment GROUP BY customer_id;

/* Get unique list of film languages under the alias language. 
Note that we are not asking you to obtain the language per each film, 
but this is a good time to think about how you might get that information 
in the future. */

SELECT distinct name from language;

/* 5.1 Find out how many stores does the company have?
5.2 Find out how many employees staff does the company have?
5.3 Return a list of employee first names only? */
SELECT count(store_id) as "Numer of stores" from store;
SELECT count(staff_id) as 'Number of staff' from staff;
SELECT first_name from staff;

