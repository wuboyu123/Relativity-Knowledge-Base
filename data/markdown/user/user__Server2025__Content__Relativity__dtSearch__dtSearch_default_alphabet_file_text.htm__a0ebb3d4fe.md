---
title: "dtSearch default alphabet file text"
url: https://help.relativity.com/Server2025/Content/Relativity/dtSearch/dtSearch_default_alphabet_file_text.htm
collection: user
fetched_at: 2026-06-22T06:16:33+00:00
sha256: cedd65e3235abd75007d9605864a0d293d6706d1f73a6d179643f913d1ffc0a8
---

dtSearch default alphabet file text Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# dtSearch default alphabet file text

Some of the characters in the alphabet file are not printable; screenshots were used instead of the actual text. You cannot copy or paste the Spaces or Ignore characters since they are not printable. Instead, use the dtSearchDefaultAlphabetFile instance setting to update the dtSearch default alphabet file.

Each sequence must start with a leading, or empty, space. Not having the leading space may produce errors.

Alphabet file validation

When you save a dtSearch index, Relativity runs a validation check on the alphabet list. You will see a warning message if Relativity detects invalid spacing or syntax. You cannot save the index if there are errors with the alphabet list. The validation check includes:

- Header sections:

-

Header section appears first in Alphabet

-

Exact header section without any added whitespace

-

Required newline before section

- Letters:

-

Exact title, allowing any whitespace and comments preceding double slash //

-

Each letter on own line with preceding space

-

Each letter variant separate by single space

-

Allow any extra whitespace after letter

- Hyphens, Spaces, and Ignore

-

Exact title, allowing any whitespace

-

Single line of characters with preceding space

-

Optional newlines before next section

- Footer sections:

-

Exact title

-

Skip validating any text following title

- General:

-

Purple, Pink, Red, Green sections are each optional and can be in any order

dtSearch Alphabet File

[Letters] // Original letter, lower case, upper case, unaccented

0 0 0 0

1 1 1 1

2 2 2 2

3 3 3 3

4 4 4 4

5 5 5 5

6 6 6 6

7 7 7 7

8 8 8 8

9 9 9 9

A a A A

B b B B

C c C C

D d D D

E e E E

F f F F

G g G G

H h H H

I i I I

J j J J

K k K K

L l L L

M m M M

N n N N

O o O O

P p P P

Q q Q Q

R r R R

S s S S

T t T T

U u U U

V v V V

W w W W

X x X X

Y y Y Y

Z z Z Z

_ _ _ _

a a A a

b b B b

c c C c

d d D d

e e E e

f f F f

g g G g

h h H h

i i I i

j j J j

k k K k

l l L l

m m M m

n n N n

o o O o

p p P p

q q Q q

r r R r

s s S s

t t T t

u u U u

v v V v

w w W w

x x X x

y y Y y

z z Z z

[Hyphens]

-

[Spaces]

\09\0a\0c\0d !@"#$&'()*+,./:;<=>?[\5c]^`{|}~

[Ignore]

[End]

CJKRanges = 0e00-0e4e 3040-30ff 4e00-9fff

Previous guidance hid some characters that should not have been hidden. Those non-printable characters are critical to index function and should never be removed. The "\08" text represents the "backspace" text, and should also never be removed or split up (IE trying to index the backslash).

This section only accepts ASCII characters (code points between 33 and 127) as input, we currently do not support ignoring extended Unicode values.

On this page

- dtSearch default alphabet file text


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
