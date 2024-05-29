# Floretum - a flower observation catalogue.

## End-user brief

I go on lots of countryside walks, and enjoy admiring the flowers as the seasons go by. I would like to document my observations of flowers in various locations throughout the year.

Every time I see a flower or group of flowers, I would like to record the flower I saw, where I saw it, when I saw it, and optionally upload a photograph. 

I would like a dashboard overview where I can see all of my recorded observations, and be able to sort them alphabetically and by time of observation.

### It would be nice if...

- There was autocomplete for the name of the flower and the location of the observation.
- I could upload a photograph of the flower I saw, and the species was recognised and populated in the name field.
- EXIF data from my photograph, if available, was used to populate the location field.
- I could view all of my recorded observations on a map.
- I could upload a group of photos and have multiple observation records be automatically created.

## Technical requirements

##### MVP

- A web app that allows users to document their observations of flowers in various locations throughout the year.
- The user will be able to:
  - Create a user account 
  - Log into their user account
  - Add an observation, inputting:
    - Flower species
    - Observation location
    - Observation time
    - Photograph of flower
  - View a list of their observations
  - Sort this list by:
    - Alphabetical order
    - Observation time
  - View individual observations
  - Edit observation data

---

##### Extensions

- Autocomplete input for flower species and observation location.
- Identify flowers from the uploaded photograph, and populate the identified species in the "Flower species" field.
- Populate the observation location and time fields using EXIF data from the uploaded photograph.
- Visualise all observations on an interactive map.

## Information overview

- **User account**
  - Username
  - Password
  - List of observations
- **Observation**
  - Observer (user account)
  - Flower species
  - Observation location
  - Observation time
  - Photograph of flower

## 











