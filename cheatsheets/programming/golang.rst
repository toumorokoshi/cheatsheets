======================
Go Language cheatsheet
======================


Primitives
==========

The following are primitives in go:

* bool
* string
* int
* int8
* int16
* int32
* int64
* uint
* uint8
* uint16
* uint32
* uint64
* uintptr
* byte
* rune
* float32
* float64
* complex64
* complex128

Standard methods
================

for loop (for loops also account for while loops):

.. code:: go

  for i := 0; i < 10; i++ {
    fmt.Println(
      pos(i),
      neg(-2*i)
    )
  }

Nice way to check for errors an operate on something:

.. code:: go

  if fileHandle, err := os.Open(filePath); err != nil {
    // handle error
  }



Conventions
===========

* Private fields and methods are lowercase, public is uppercase
* comments: // single line

.. code:: go

  /* 
   this is a multiline comment
   */


Structs
=======

initializing a struct:

.. code:: go

  type MyStruct struct {
    elementA string
    elementB int
    ElementC uint // capitalize for public access
  }

Adding a method:

.. code:: go

  func (m *MyStruct) Method string {
    return m.elementA
  }
