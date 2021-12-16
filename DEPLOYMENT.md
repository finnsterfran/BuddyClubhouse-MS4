## Github
### Project Setup: 
    * Make new repository in github
    * Select Code Institute Full Template
    * Name and create the repository
    * On repository page, click green GITPOD button to launch gitpod
        * this made it unnecessary to run initialisation `git init`
    * Throughout the project:
        * `git add .` to add files to stage.
        * `git commit -m "commit message"`
        * `git push` to push changes to main in github
<p>&nbsp;</p>

## Gitpod
### Project Setup:
    * I opted to use python-decouple to hide my secret_keys 
    * create a folder .env 
    * add secret keys without '' and no spacing after = 
        * e.g. S_KEY=kdfplgksdgdfgjkdpgsgso444 
    * in settings.py add `from decouple import config
        * set up secret key : SECRET_KEY = config('S_KEY')
<p>&nbsp;</p>

## Heroku
#### Set up:
1.  In Gitpod, set up files that Heroku will need:
    *   requirements.txt specifies what packages(python) are needed for this app.
    *   This can be created in the terminal like so :`pip3 freeze > requirements.txt
    *   A Procfile is needed to specify to Heroku where it should look to kick start this app. 
        * A package called GUNICORN needs to be installed
        * Procfile contains this line of code: `web: gunicorn buddy_program.wsgi:application`
    *   push these changes to github
<p>&nbsp;</p>

2. Make a new app in Heroku:
    * Create an account if one doesn't already exist
    * Create new app > select region > in resources, select Heroku Postgres
<p>&nbsp;</p>

3. The old database.
#### In development, the project used sqlite3 for database. The data here needs to be moved to the Heroku Postgres database. As I didn't use any fixtures, I needed to find a way to download the database into a json file and then unload it to Heroku Postgres
#### So, to backup current database into a json file:
    * `python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`
<p>&nbsp;</p>

4. The new database:
#### Some steps to take to get Heroku wired up:
    * `pip3 install dj_database_url`
    * `pip3 install psycopg2-binary
    * in settings.py 
        * import dj_database_url
        * comment out default database
        * add new default database: 
            * DATABASES = {'default': dj_database_url.parse('database_url_key_from_heroku_goes_in_here')}
    * migrate models to the new database:
        * `python3 manage.py migrate`
    * load data from old database:
        * `python3 manage.py loaddata all json`
    * create a new superuser(because the new DB does not inherit the superuser of the old DB)
        * `python3 manage.py createsuperuser
    * Set up new DATABASES configuration: 
        *   if 'DATABASE_URL' in os.environ:
            print('using Postgres') << This isn't required, it lets me know which database is being used 
            DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) << this key is in Heroku settings>config vars
            }
            else:
                print('unable to find database_url, using sqlite DB')
                DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
<p>&nbsp;</p>

#### Heroku CLI login:
    * heroku login -i
    * enter my account email
    * enter the api token as my password
    * if unsure if you're logged in, type : `heroku auth:whoami`
<p>&nbsp;</p>

5. The Heroku settings
#### With Heroku logged in, there were some settings to make:
    * Disallow collection of static files because we want to store them on Amazon AWS
        * `heroku config:set DISABLE_COLLECTSTATIC=1`
    * Give our new heroku app permission to our project:
        * in settings.py, add the following settings to ALLOWED HOST:
            * `ALLOWED_HOSTS = ['the-buddy-clubhouse-ms4.herokuapp.com', 'localhost']`
    * change secret keys set up in Heroku config var: 
        SECRET_KEY = os.environ.get('SECRET_KEY', '')
        DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
        STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', '')
        STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
        STRIPE_CURRENCY = 'eur'
        STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET', '')
    * COMMIT all changes to github 
    * git push heroku main
    * Heroku starts to build. 
<p>&nbsp;</p>

#### Back in Heroku account page, let's connect for automatic push to heroku when pushing to github:
    * open deploy 
    * click connect to github
    * search for the right repository
    * connect to the repository and enable automatic deploys

## AWS
#### Amazon AWS S3 is where the static and media files from the project are stored. 
1.  Create an account if you don't have one.
<p>&nbsp;</p>
2.  Creating a bucket
#### Search for S3 (scalable)
    * click create bucket, name the bucket and pick a region that is closest (I chose EU.frankfurt)
    * uncheck block access
        * acknowledge what this setting entails (this bucket is public)
<p>&nbsp;</p>

3.  Bucket settings
#### Some setting to get the bucket configured properly:
    * in index and error, we use the default index.html and error.html
    * Permissions(CORS), we add these lines:
        [ 
            {"AllowedHeaders":[
                "Authorization"
            ],
            "AllowedMethods":[
                "GET"
            ],
            "AllowedOrigins:[
                "*"
            ],
            "ExposedHeaders":[]
            }
        ]
    * Click bucket policy and generate policy
        * Select a type: S3 bucket policy
        * Statements: 
            * Effects : allow
        * AWS Service: Amazon S3
        * Action: GetObject
        * Copy ARN (available on the previous page) and paste it in
        * Click add statement
        * Click button to generate policy
        * Copy and add this policy to bucket policy editor
        * include /* to the end of the resources key
        * SAVE
<p>&nbsp;</p>

4. IAM (Identity and Access Management)
#### We need to create a user group that our user can sit in to accesses the bucket, for which we use IAM
    * search for IAM in services
    * click create group
        * enter a name for the group 
        * create the group
    * now create a policy
        * click create a policy
        * select the JSON tab and import managed policies
        * search for AmazonS3FullAccess policy, import that
        * back in the JSON tab, we need to make some access changes to the policy we just imported:
            * we go to S3 to get our ARN 
            * we paste the ARN into the "Resource", like so: 
                "Resource": [
                    "arn:aws:s3:::thisisthenameofthebucket",
                    "arn:aws:s3:::thisisthenameofthebucket/*"
                ]
            * click review policy
            * name the policy and give it a description
            * click create policy
    * attach policy to the user group that was just made:
        * go to groups
        * choose the group we made
        * click attach policy
        * find the policy that was just made
        * select and attach policy
    * now create a user to put in the group:
        * click users
        * add user
        * create a user with programmatic access
        * add user to group by selecting the group 
        * click all the way through to create user
        * create user
        * !important - Download the csv file which contains AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
<p>&nbsp;</p>

5. CONNECTING DJANGO TO OUR NEWLY CREATED BUCKET
#### We need to install two packages for this:
    * `pip3 install boto3`
    * `pip3 install django-storages`
    * `pip3 freeze > requirements.txt`
<p>&nbsp;</p>

#### We add 'storages' to installed apps in setting.py 
<p>&nbsp;</p>

#### To connect django to S3, we need to add some settings, but as this will only be added on Heroku, we need to write an if statement for django to run a check and get the details from there:
    * if 'USE_AWS' is os.environ:
        AWS_STORAGE_BUCKET_NAME = 'thebucketname'
        AWS_S3_REGION_NAME = 'eu-central-1' << because my bucket's region is EU.Frankfurt
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
    * now we go to Heroku to add some variables to the config:
        * add AWS_ACCESS_KEY_ID
        * add AWS_SECRET_ACCESS_KEY
        * add USE_AWS to be True
        * we remove DISABLE_COLLECTSTATIC from the variables
<p>&nbsp;</p>

#### Because now that static is being collected again, we need a place to store these static files:
    * create a new file called custom.storages.py 
    * include:
        * from django conf import settings
        * from storages.backends.s3boto3 import S3Boto3Storage
        * create classes to tell Django where to store the files:
            * class StaticStorage(S3Boto3Storage):
                location = settings.STATICFILES_LOCATION
            * class MediaStorage(S3Boto3Storage):
                location = settings.MEDIAFILES_LOCATION
    * add this storage setting to settings.py:
        *   STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'
    * setting to override URLS in production: 
        *   STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
#### Push to github (which will automatically push to Heroku since we've configured it so!)
<p>&nbsp;</p>

#### Finally, manually upload all the media files to the AWS bucket via the AWS dashboard itself.
<p>&nbsp;</p>

## Setting this project up locally
#### In github, click the button that reads CODE, you can: 
    * download ZIP to get a copy of the repository
    * extract the zip file
    * or clone this repository `git clone https://github.com/finnsterfran/BuddyClubhouse-MS4.git`
