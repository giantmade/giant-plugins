## 1.0.18
- Added anchor_id field to the templates.

## 1.0.17
- Added anchor_id field to the Content Width Video, Donate, Page Card Block, and Rich Text plugins.

## 1.0.16
- Added cta option for rich text plugin.

## 1.0.15
- Revert changes made in 1.0.12 due to error when assiging internal link.

## 1.0.13
- Remove explicit `fields` definition so we rely on `exclude` instead 

## 1.0.12
- Override PageCard form so it uses the SmartLinkWidget (select2 for internal pages)

## 1.0.11
- Improve PageCard str method by showing the title of the internal page if it's present, failing
  that show the title or the pk
- Add a few methods to determine if the Internal Page associated with a PageCard is published

## 1.0.5
- Make "title" field on page card child plugin optional

## 1.0.4
- Make "caption" field on content width video plugin mandatory
- Make "credit" and "credit" fields on content width image plugin mandatory

## 1.0.3
- Add "caption" field to content width video plugin
- Add "credit" field to content width image plugin

## 1.0.2
- Change pullqoute and logo grid image fields on_delete value to set_null

## 1.0.1
- Update the "quote" field to be Rich text rather than standard text
- Add a left/right align option for the text

## 1.0.0-beta.1

- Refactor migrations structure so each plugin module has it's own migrations folder
- Add individual plugins to settings file for new migration structure
- Update README with new installation instructions

## 1.0.1
- Update the "quote" field to be Rich text rather than standard text
- Add a left/right align option for the text
