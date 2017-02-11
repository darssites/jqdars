# jqdars
We all love jQuery (Most of us do). If only you could use it with dars...

# How-to

### Step 1

Clone the code:

     git clone http://github.com/darssites/jqdars
     
### Step 2

Open the "jqdars" folder, and then copy the "jqdars" folder **inside of that** into the plugins folder of your dars project. 

### Step 3

To add jquery to your site for use with the JScript class, add this code to your imports:

    from plugins.jqdars.jqdars import jqdars
    
Then, create a jQuery object like so:

    j = JQuery()
    
That will use the latest version. If you want version 3.3, for instance, you go:

    j = JQuery("3.3")
    
After you've got all of that sorted out, simply append to your page.

    page.append(j)
    
Voila!
