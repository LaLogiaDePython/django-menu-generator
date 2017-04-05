## 1.0.0

Feature:

  - Dropped support for Django < 1.8
  - Dropped support for Python < 3.4
  - Changed licensing from BSD to MIT
  - Added `validators` feature
    - Not backward compatible with versions < 1.0.0

## 0.1.10

Feature:

  - Added `render_for_user_when_condition_is_false` feature

## 0.1.9

Enhancement:

  - Process breadcrumbs based on nodes and not partial paths

## 0.1.8

BugFix:

  - Properly handle `render_for_user_when_condition_is_true` submenu(s)

## 0.1.7

Enhancement:

  - pass the `request` object to the `render_for_user_when_condition_is_true` method instead of the `user` object

## 0.1.6

Feature:

  - Added `render_for_user_when_condition_is_true` feature

## 0.1.5

Enhancement:

  - Updated travis to include Django 1.9


## 0.1.4

BugFix:

  - Added menu `depth` to item. top-nav: depth=0, sub-nav: depth=1 etc.


## 0.1.3

BugFix:

  - Skip breadcrumbs for empty list


## 0.1.2

BugFix:

  - Recalculate active state for all objects, including the out-of-focus ones.


## 0.1.1

Features:

  - Allow any menu name be loaded directly from the settings, bypassing MENUWARE_MENU.


## 0.1.0

Features:

  - Added template tags to load up menus from the setting.py


## 0.0.4

Enhancement:

  - Added usage to README


## 0.0.3

Enhancement:

  - Added More Test Cases
  - Clean up


## 0.0.2

Enhancement:

  - Added Test Cases


## 0.0.1

Features:

  - Initial Release
