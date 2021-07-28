# MongoDb Cheatsheet

- No Sql Database, Data is stored in BSON Format(Binary Json)

# Database Commands

- View  all Databases
    > show dbs

    - admin   0.000GB
    - config  0.000GB
    - local   0.000GB
    - mydb    0.000GB
- Create or Switch to database
    > use mydatbase
    - switched to db mydatbase
- Viewing Current Database Name
    > db
    - mydatabase
- Deleting Database ({ "ok" : 1 })
    > db.dropDatabase()

# Collection Commands (Columns)

- Create Collection
    > db.createCollection('Courses')
- View Collections
    > show collections
- Remove Collections (returns true)
    > db.Courses.drop()

# Documents (rows) Commands

- Insert Document(Row)
    ```json
    > db.Users.insert({
        "name": "Arbaaz",
        "job": "Full stack Developer",
        "working_at": "Startup"
        })
    
    -Output
        WriteResult({ "nInserted" : 1 })
    ```
- Insert Multiple Documents
    ```json
    > db.Users.insertMany([
        {
            "name": "Vinith",
            "job": "eTMF Speacialist",
            "working_at": "TCS"
        },
        {
            "name": "Shiva",
            "job": ".Net Developer",
            "working_at": "eExpedise"
        }
    ])

    Output
    {
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("6100fa1280b8b18da96d0c91"),
                ObjectId("6100fa1280b8b18da96d0c92")
        ]
    }
    ```
- Show all rows in collection
    > db.Users.find()

    > db.Users.find().pretty()
    ```json
    {
            "_id" : ObjectId("6100f82180b8b18da96d0c90"),
            "name" : "Arbaaz",
            "job" : "Full stack Developer",
            "working_at" : "Startup"
    }
    {
            "_id" : ObjectId("6100fa1280b8b18da96d0c91"),
            "name" : "Vinith",
            "job" : "eTMF Speacialist",
            "working_at" : "TCS"
    }
    {
            "_id" : ObjectId("6100fa1280b8b18da96d0c92"),
            "name" : "Shiva",
            "job" : ".Net Developer",
            "working_at" : "eExpedise"
    }
    ```
- Find the first row  matching object
    > db.Users.findOne()

    > db.Users.findOne({"name": "Shiva"})
    ```json
    {
            "_id" : ObjectId("6100fa1280b8b18da96d0c92"),
            "name" : "Shiva",
            "job" : ".Net Developer",
            "working_at" : "eExpedise"
    }
    ```

# Searching in Database

- Search using object fields
    > db.Users.find({"job": "eTMF Specialist"})

    > db.Users.find({"job": "eTMF Speacialist"}).pretty()
    ```json
    {
        "_id" : ObjectId("6100fa1280b8b18da96d0c91"),
        "name" : "Vinith",
        "job" : "eTMF Speacialist",
        "working_at" : "TCS"
    }
    ```
- Limiting output printed on console (eg. 2 rows)
    > db.Users.find().limit(2)

- Count number of rows
    > db.Users.count()
    - 3

    > db.Users.find().limit(2).count()
    - 3 (limit only changes the output printed)

- Updating Rows
    ```json
    > db.Users.update({"name": "Vinith"}, {
        "name": "Vinith",
        "job": "eTMF Specialist",
        "working_at": "TCS",
        "experience": 3
        })

    - Output
    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
    
    - nUpserted specifies if anything is inserted if not found matching object
    > db.Users.update({"name": "Harish"}, {
        "name": "Harish",
        "job": "Cyber Security Analyst",
        "working_at": "Infosys",
        "experience": 1
        }, {upsert: true})

    - Output (1 row inserted)
    WriteResult({
        "nMatched" : 0,
        "nUpserted" : 1,
        "nModified" : 0,
        "_id" : ObjectId("61010ce874cadd30362625de")
    })
    ```

- Sorting the output (1 for ascending, -1 for descending)
    ```json
    > db.Users.find().sort({"experience": 1})
    > db.Users.find().sort({"experience": -1}).pretty()
    {
        "_id" : ObjectId("6100fa1280b8b18da96d0c91"),
        "name" : "Vinith",
        "job" : "eTMF Specialist",
        "working_at" : "TCS",
        "experience" : 3
    }
    {
        "_id" : ObjectId("61010ce874cadd30362625de"),
        "name" : "Harish",
        "job" : "Cyber Security Analyst",
        "working_at" : "Infosys",
        "experience" : 1
    }
    {
        "_id" : ObjectId("6100f82180b8b18da96d0c90"),
        "name" : "Arbaaz",
        "job" : "Full stack Developer",
        "working_at" : "Startup"
    }
    {
        "_id" : ObjectId("6100fa1280b8b18da96d0c92"),
        "name" : "Shiva",
        "job" : ".Net Developer",
        "working_at" : "eExpedise"
    }
    ```

# Operators
- increment ($inc), if the attribute is not present it wil automatically add
    > db.Users.update({"name": "Arbaaz"},{$inc: { "experience": 1}})
    
    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })

    > db.Users.find({"name": "Arbaaz"})

    { "_id" : ObjectId("6100f82180b8b18da96d0c90"), "name" : "Arbaaz", "job" : "Full stack Developer", "working_at" : "Startup", "experience" : 1 }

- Rename columns
    > db.Users.update({"name": "Arbaaz"}, {$rename: {experience: "exp"}})

        WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })


    > db.Users.find({"name": "Arbaaz"})

        { "_id" : ObjectId("6100f82180b8b18da96d0c90"), "name" : "Arbaaz", "job" : "Full stack Developer", "working_at" : "Startup", "exp" : 2 }

    > db.Users.updateMany({}, {$rename: {experience: "exp"}})

        { "acknowledged" : true, "matchedCount" : 4, "modifiedCount" : 2 }

- less than($lt), >($gt), <=($lte), >=($gte)
    > db.Users.find({"exp": {$lte:1}})

        { "_id" : ObjectId("61010ce874cadd30362625de"), "name" : "Harish", "job" : "Cyber Security Analyst", "working_at" : "Infosys", "exp" : 1 }

- string search using regex (returns all users whose job is Developer)
    > db.Users.find({"job": /Developer/})
        { "_id" : ObjectId("6100fa1280b8b18da96d0c92"), "name" : "Shiva", "job" : ".Net Developer", "working_at" : "eExpedise" }
        { "_id" : ObjectId("6101149a80b8b18da96d0c93"), "name" : "Arbaaz", "job" : "Full stack Developer", "working_at" : "Startup", "exp" : 1 }

# Deleting rows
> db.Users.remove({"name": "Arbaaz"})

    WriteResult({ "nRemoved" : 1 })


{
"name" : "Arbaaz",
"job" : "Full stack Developer",
"working_at" : "Startup"
"exp": 1
}