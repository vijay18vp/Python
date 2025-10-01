# Python Notes – Part 1: Lists

## 1. Introduction to Lists

* Lists in Python are **ordered collections** used to store multiple items in a single variable.
* They are similar to arrays in other languages.

**Syntax:**

```python
my_list = [1, 2, 3, "hello", 4.5]
```

**Properties of Lists:**

* **Mutable**: You can change, add, or remove elements.
* **Index-based Access**: Elements can be accessed using indexes.

```python
my_list = ["apple", "banana", "cherry"]
print(my_list[0])   # apple
print(my_list[1])   # banana
print(my_list[2])   # cherry
```

---

## 2. Common List Functions / Methods

### 2.1 append()

* Adds an element at the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)   # ['apple', 'banana', 'cherry']
```

### 2.2 insert()

* Inserts an element at a specific index.

```python
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)   # ['apple', 'orange', 'banana']
```

### 2.3 remove()

* Removes the first occurrence of a specified element.

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)   # ['apple', 'cherry']
```

### 2.4 clear()

* Removes all elements from the list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)   # []
```

### 2.5 pop()

* Removes and returns the last element (or element at a given index).

```python
fruits = ["apple", "banana", "cherry"]
fruits.pop()       # removes "cherry"
print(fruits)      # ['apple', 'banana']

fruits.pop(0)      # removes "apple"
print(fruits)      # ['banana']
```

### 2.6 sort()

* Sorts the list in ascending order (by default).

```python
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)   # [1, 2, 3, 4]
```
