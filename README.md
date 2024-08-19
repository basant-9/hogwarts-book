# hogwarts-book
Overview
---
## Project Description :
the project includes classes , to manage 
**`MagicalContact`**: Base class 
**`WizardOrWitch`**: Inherits from `MagicalContact` , includes wand and houses 
**`MagicalCreature`**: Inherits from `MagicalContact`, includes species and tame.
**`MagicalContactBook`**: Manages `MagicalContact`

## Class Descriptions

### `MagicalContact`
- **Attributes:**
  - `name`
  - `email`
  - `phone_number`
- **Methods:**
  - `get_name()`: Returns the name
  - `get_email()`: Returns the email
  - `get_phone_number()`: Returns the phone number
  - `set_email(email)`: Updates the email
  - `set_phone_number(phone_number)`: Updates the phone number
  - `describe()`: Print

### `WizardOrWitch` 
- **Attributes:**
  - `__wand`: core, wood, length
  - `__house`: Hogwarts house.
- **Methods:**
  - `get_wand()`: Returns wand details
  - `get_house()`: Returns the house
  - `describe()`: Print

### `MagicalCreature`
- **Attributes:**
  - `__species`: Species 
  - `__is_tame`:yes or no 
- **Methods:**
  - `get_species()`: Returns the species
  - `is_tame()`: Returns tame
  - `describe()`: Print

### `MagicalContactBook`
- **Attributes:**
  - `__contacts`: list 
- **Methods:**
  - `add_contact(contact)`: Adds a contact
  - `list_contacts()`: Lists all contacts
  - `find_contact(name)`: print & search 
