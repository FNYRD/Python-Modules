# Python Piscine — 42 School

**User:** `jericard`

This repository contains the completed modules from the **42 School Python Piscine**. Each module introduces a new set of skills, building upon the previous ones to progressively master the language.

---

## Index

- [Module00 — Python Fundamentals](#module00--python-fundamentals)
- [Module01 — Object-Oriented Programming](#module01--object-oriented-programming)
- [Module02 — Exception Handling](#module02--exception-handling)
- [Module03 — Advanced Data Structures](#module03--advanced-data-structures)
- [Module04 — File Input/Output](#module04--file-inputoutput)
- [Module05 — Abstract Classes and Polymorphism](#module05--abstract-classes-and-polymorphism)
- [Module06 — Packages and Module System](#module06--packages-and-module-system)
- [Module07 — Advanced Design Patterns](#module07--advanced-design-patterns)
- [Module08 — Virtual Environments and Configuration](#module08--virtual-environments-and-configuration)
- [Module09 — Data Validation with Pydantic](#module09--data-validation-with-pydantic)
- [Module10 — Functional Programming](#module10--functional-programming)

---

## Module00 — Python Fundamentals

**Objective:** Introduction to basic Python syntax. Covers defining functions with type annotations, handling variables, reading user input, applying conditionals, iterating with loops, formatting strings with f-strings, and building both iterative and recursive solutions. The exercises follow a garden and harvest theme.

| Exercise | Main concept |
|----------|-------------|
| `ft_hello_garden.py` | Function definition and type annotations |
| `ft_plot_area.py` | Variables, user input, and arithmetic |
| `ft_harvest_total.py` | Summing multiple inputs |
| `ft_plant_age.py` | `if/else` conditionals |
| `ft_water_reminder.py` | More conditionals with numeric comparisons |
| `ft_count_harvest_*.py` | `for` loops vs. recursion |
| `ft_garden_summary.py` | String formatting with f-strings |
| `ft_seed_inventory.py` | Functions with multiple parameters and conditional logic |

---

## Module01 — Object-Oriented Programming

**Objective:** Master the pillars of OOP in Python. Covers designing classes with `__init__` and `__str__`, applying encapsulation through private attributes and getters/setters, building inheritance hierarchies using `super()`, and exploring static methods, class methods, and nested classes. The entire module uses a plant and garden ecosystem as its metaphor.

| Exercise | Main concept |
|----------|-------------|
| `ft_garden_intro.py` | Script structure with `if __name__ == "__main__"` |
| `ft_garden_data.py` | Basic class with `__init__` and `__str__` |
| `ft_plant_growth.py` | Instance methods that modify state |
| `ft_plant_factory.py` | Creating multiple instances and typed lists |
| `ft_garden_security.py` | Encapsulation: private attributes, getters and setters |
| `ft_plant_types.py` | Multiple inheritance: `Plant → Flower`, `Tree`, `Vegetable` |
| `ft_garden_analytics.py` | Nested classes, static methods, class methods, polymorphism |

---

## Module02 — Exception Handling

**Objective:** Learn to write robust code through Python's exception system. Covers `try/except` blocks for specific error types, the `finally` clause to guarantee cleanup, using `raise` to throw exceptions manually, and creating custom exception hierarchies that inherit from `Exception`. The context is a garden management system with watering and plant health errors.

| Exercise | Main concept |
|----------|-------------|
| `ft_first_exception.py` | Basic `try/except`, `ValueError`, error codes |
| `ft_different_errors.py` | Multiple exception types in a single block |
| `ft_custom_errors.py` | Custom exception classes with inheritance (`GardenError`, `PlantError`, `WaterError`) |
| `ft_finally_block.py` | `finally` clause for guaranteed cleanup |
| `ft_raise_errors.py` | Explicit `raise` with descriptive messages |
| `ft_garden_management.py` | Combining all concepts: error recovery patterns |

---

## Module03 — Advanced Data Structures

**Objective:** Explore Python's native collections beyond lists: tuples, sets, and nested dictionaries. Also covers command-line arguments (`sys.argv`), generators with `yield`, and all three comprehension forms (list, dict, and set comprehensions). The theme revolves around video game analytics.

| Exercise | Main concept |
|----------|-------------|
| `ft_command_quest.py` | `sys.argv`, argument parsing |
| `ft_score_analytics.py` | Lists: sum, average, min, max |
| `ft_coordinate_system.py` | Tuples, unpacking, 3D distance calculation |
| `ft_achievement_tracker.py` | Sets: union, intersection, difference |
| `ft_inventory_system.py` | Nested dictionaries, iteration, `.items()` |
| `ft_data_stream.py` | Generators with `yield` (primes, Fibonacci, events) |
| `ft_analytics_dashboard.py` | List, dictionary, and set comprehensions |

---

## Module04 — File Input/Output

**Objective:** Handle text files and I/O streams in Python. Covers opening modes (`r`, `w`), the importance of closing files correctly, using context managers (`with`) as best practice, accessing standard streams (`sys.stdin`, `sys.stdout`, `sys.stderr`), and handling file access errors such as `FileNotFoundError` and `PermissionError`. The theme is a file archive and vault system.

| Exercise | Main concept |
|----------|-------------|
| `ft_ancient_text.py` | Reading files with `open()` and manual close |
| `ft_archive_creation.py` | Writing files and `FileExistsError` |
| `ft_stream_management.py` | `sys.stdin`, `sys.stdout`, `sys.stderr`, `readline()` and `write()` |
| `ft_vault_security.py` | Context managers (`with`) for safe file handling |
| `ft_crisis_response.py` | Multiple exceptions: `FileNotFoundError`, `PermissionError` |

---

## Module05 — Abstract Classes and Polymorphism

**Objective:** Deepen OOP knowledge through abstract base classes (`ABC`) that define mandatory interfaces. Covers implementing multiple concrete classes that fulfill the same contract, practicing true polymorphism (a function works with any subtype without knowing it), and introducing duck typing with `Protocol` for composition without inheritance. The scenario is a data processing pipeline with different input types.

| Exercise | Main concept |
|----------|-------------|
| `data_processor.py` | `ABC`, abstract methods, three concrete implementations (`NumericProcessor`, `TextProcessor`, `LogProcessor`) |
| `data_stream.py` | Polymorphic orchestrator, `@staticmethod` for validation, automatic routing |
| `data_pipeline.py` | Duck typing with `Protocol`, CSV and JSON export plugins |

---

## Module06 — Packages and Module System

**Objective:** Understand how Python organizes code into packages and modules. Covers different import styles (`import module`, `from module import name`), subpackage structure with `__init__.py`, controlled symbol exposure with `__all__`, and import aliasing. The module uses an alchemy package (`alchemy`) with subpackages for spells and recipes.

| Exercise | Main concept |
|----------|-------------|
| `ft_alembic_0.py` / `ft_alembic_1.py` | `import module` vs. `from module import name` |
| `ft_distillation_*.py` | Imports from nested subpackages |
| `ft_transmutation_*.py` | Full namespace paths in deep hierarchies |
| `alchemy/__init__.py` | `__all__`, aliasing with `as`, re-exporting subpackages |

---

## Module07 — Advanced Design Patterns

**Objective:** Apply classic software engineering design patterns in Python. Covers the **Factory Pattern** (creating objects without specifying the concrete class), the **Mixin Pattern** (adding capabilities through multiple inheritance), and the **Strategy Pattern** (encapsulating interchangeable algorithms). The scenario is a Pokémon-style creature battle system.

| Exercise | Main concept |
|----------|-------------|
| `ex0/` — `battle.py` | Factory Pattern: `CreatureFactory`, `FlameFactory`, `AquaFactory` |
| `ex1/` — `capacitor.py` | Mixin interfaces: `HealCapability`, `TransformCapability`, multiple inheritance |
| `ex2/` — `tournament.py` | Strategy Pattern: `NormalStrategy`, `DefensiveStrategy`, `AggressiveStrategy`, `isinstance()` for dynamic dispatch |

---

## Module08 — Virtual Environments and Configuration

**Objective:** Master the infrastructure needed for real Python projects. Covers creating and detecting virtual environments (`venv`), managing dependencies with `pip` and `poetry`, consuming external APIs with `requests`, analyzing data with `pandas` and `numpy`, generating charts with `matplotlib`, and handling sensitive configuration through environment variables with `python-dotenv`. The theme is the Matrix universe.

| Exercise | Main concept |
|----------|-------------|
| `construct.py` | Virtual environment detection, `sys.prefix`, `site.getsitepackages()` |
| `loading.py` | Dependencies with `importlib.metadata`, Binance API, data analysis with pandas/numpy, visualization with matplotlib |
| `oracle.py` | Environment variables with `dotenv`, environment-based config (dev/prod), secret validation |

---

## Module09 — Data Validation with Pydantic

**Objective:** Use Pydantic v2 to guarantee data integrity in Python. Covers creating models with `BaseModel`, declaring field constraints with `Field` (numeric ranges, string lengths, default values), defining `Enum` for controlled values, building custom validators with `@model_validator` for cross-field business rules, and composing nested models with collection-level validation. The scenario is a space station.

| Exercise | Main concept |
|----------|-------------|
| `ex0/space_station.py` | `BaseModel`, `Field` with `ge`, `le`, `min_length`, `model_validate()`, `ValidationError` |
| `ex1/alien_contact.py` | `Enum`, `@model_validator(mode='after')`, cross-field validations |
| `ex2/space_crew.py` | Nested models (`List[CrewMember]`), collection validators, experience and leadership rules |

---

## Module10 — Functional Programming

**Objective:** Master the functional programming paradigm in Python. Covers lambda functions, `filter()`, `map()`, and `sorted()` with custom keys; building higher-order functions that receive and return functions; exploring closures and the `nonlocal` keyword for encapsulated state; using the `functools` module (`reduce`, `partial`, `lru_cache`, `singledispatch`); and implementing decorators with and without parameters using `@functools.wraps`. The context is a world of wizards and spells.

| Exercise | Main concept |
|----------|-------------|
| `ex0/lambda_spells.py` | Lambdas, `sorted()`, `filter()`, `map()`, `max()`, `min()` with key functions |
| `ex1/higher_magic.py` | Higher-order functions, composition, `Callable` type hints |
| `ex2/scope_mysteries.py` | Closures, `nonlocal`, stateful functions, functional factory pattern |
| `ex3/functools_artifacts.py` | `reduce`, `partial`, `lru_cache`, `singledispatch` |
| `ex4/decorator_mastery.py` | Simple and parameterized decorators, `@functools.wraps`, timer, validator, retry |

---

*42 School — Python Piscine | jericard*
