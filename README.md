# Review Scrapper

## When to use reviewScrapper
  If you wants to have a deep dive into the product quality of any item just use our product.

## How to use Review Scrapper
 - Visit the deployed portal at https://reviewscrapperpy.herokuapp.com/
 - Provide the product name for which you wants to get reviews as an overview.
 - Click on submit
 - Wait untill we collect the result from best in class E-commerce portals.
 - Click on 'Your result is ready click here' button once available to view your results.
 - Just this - Enjoy your result.

## How run the tool on local using Docker
 - Install docker over your system and clone the repo...
 - Open CMD/terminal/powershell and navigate to the root location of the repo... where Dockerfile is available.
 - Run <b>docker build -t reviewScrapper . </b>.
 - Above command will add an docker image to your local named as reviewScrapper. You can change the name as required.
 - Run the docker container using the image created in earlier step via 
   <b> docker container run --publish 8000:8000 --name reviewScarpper reviewScrapper </b>
 - Now, you can access the tool on <b> http://localhost:8000/ </b>.


## Future integrations
 - We will integrate an review summarizer really soon so that no need to look in individual reviews just go for summarized one.
 - We will add some really cool visuallization for overall rating trend for every product come with search.

## Documentation
 - https://reviewscrapperpy.herokuapp.com/docs/
 - https://reviewscrapperpy.herokuapp.com/redoc/

## Tech Stack involved
 - Python, FastAPI
 - JavaScript, JQuery
 - Web Scrapping , BS4
 - HTML5, CSS3, BootStrap4
 - RestFul API's
 - Docker
