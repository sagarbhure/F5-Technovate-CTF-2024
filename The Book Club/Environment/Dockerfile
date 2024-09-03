# Use an official PHP runtime as a parent image
FROM php:7.4-apache

# Set the working directory
WORKDIR /var/www/html

# Install required dependencies, including SQLite3
RUN apt-get update && \
    apt-get install -y libsqlite3-dev && \
    docker-php-ext-install pdo_sqlite

# Copy the current directory contents into the container at /var/www/html
COPY . /var/www/html/

# Ensure the SQLite database directory exists and is writable by the Apache user
RUN mkdir -p /var/www/html/db && \
    chown -R www-data:www-data /var/www/html/db && \
    chmod -R 775 /var/www/html/db

# Expose port 9997
EXPOSE 9997

# Start Apache service
CMD ["apache2-foreground"]
