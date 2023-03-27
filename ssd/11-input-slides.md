% Secure Software Design
% Andey Robins
% Spring 23 - Week 11

# Input Handling

## Outline

- Untrusted Input
- Input Validation
- Vulnerabilities
- Mitigation
- Fuzz Testing

## Untrusted Input

**Untrusted Input** are inputs out of your control (i.e. able to be manipulated by an attacker)

These are values you **should not trust**, in other words, they draw a trust boundary in their wake.

## Input as a Threat Vector

What is the most wide open input vector in the world?

$$ $$

**The Internet**

_"Doing a better job at input validation is perhaps the most impactful low-hanging fruit available to developrs for reducing vulnerabilities."_

## Input Validation

Several approaches:

1. Bounds checking
2. Specify encodings
3. Escaping

## Determining Validity

Obviously, the first step in validating input is to define valid conditions.

_"What usually works well is to establish an explicit limit on inputs and then leave plenty of headroom on the implementation to be certain of correctly processing all valid inputs."_

## Example: Guess-my-number

```rs
println!("Enter a number between 1-100")
let mut input_line = String::new();
io::stdin()
    .read_line(&mut input_line)?;
let guess: ??? = input_line.trim().parse()?;
```

## Example: Guess-my-number

We can use the max size to make sure any number input is able to be stored.

```rs
println!("Enter a number between 1-100")
let mut input_line = String::new();
io::stdin()
    .read_line(&mut input_line)?;
let guess: i64 = input_line.trim().parse()?;
```

## Example: Guess-my-number

But we only need to hold values from 1 to 100, so using the smallest possible size to indicate our intent may be better. This also includes some minor validation already.

```rs
println!("Enter a number between 1-100")
let mut input_line = String::new();
io::stdin().read_line(&mut input_line)?;
let guess: u8 = input_line.trim().parse()?;
```

## Validation Criteria

Several overlaid criteria are checked to ensure the validity of input.

1. Use the definition of "validity" you put together in the last step
2. Check the size of your input
3. Check other common bounds

## The XML "Zip Bomb"

4 GB in only a few lines of code.

```xml
<!DOCTYPE dtd[
    <!ENTITY big1 "big!">
    <!ENTITY big2 "&big1;&big1;&big1;&big1;&big1;
        &big1;&big1;&big1;">
    <!-- ... -->
    <!ENTITY big8 "&big7;&big7;&big7;&big7;&big7;
        &big7;&big7;&big7;">
]>
<mega>&big8;&big8;&big8;&big8;&big8;&big8;
    &big8;&big8;</mega>
```

## Common Criteria: Numbers

- range of datatype
- precision of floats
- size

## Common Criteria: Strings

- encoding schema
- length
- special characters
- potentially syntax

## Aside: Bytes vs Characters

_"I recommend specifying maximum string lengths in characters rather than bytes, if only so that non-programmers have some hope of knowing what this constraint means."_ - Kohnfelder

_"I recommend specifying maximum string lengths in bytes rather than characters, otherwise, you're waiting for UTF-8/16 to come wreck your application."_ - Andey

## Rejection of Invalid Input

What is the rule for swimming in the ocean?

_**When in doubt, don't go out.**_

## Rejection of Invalid Input

Applying that rule, when in doubt, reject the input.

Complete acceptance and rejection is the cleanest and easiest to reason about.

## Rejection Best Practices

1. Explain what constitutes a valid entry
2. Flag as many errors at once as possible
3. Have clear, simple rules for human input
4. Break up extended input into parts

## Correcting Invalid Input

Humans are not computer [citation needed]. So strict input rules are not always the easiest for us to handle.

Attempting to correct erroneous inputs is a great way to increase the availability of your system.

## Example: Phone Number Input

```js
function adddashes() {
  f = document.getElementById('phone');
  f.value = f.value.slice(0, 3) + "-" + 
            f.value.slice(3, 6) + "-" + 
            f.value.slice(6, 10);
}
```

## Best Practices

1. Remove syntactic requirements to make input easier
2. Present "best gueses" for the user to select from
3. Format their input as they provide it

## Validation Challenges

1. How do we validate a phone number input of 11 digits?
2. How do we validate a username with Katakana?
3. How do we validate an email is valid during signup?

## Input Vulnerabilities

## Injection Vulnerabilities

## Mitigation

## Fuzzing