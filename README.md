 # Backend Engineer Test

This is a power test and is meant to be submitted within 48 hours of receipt. We expect that you implement all tasks in the same project using Python.

You will be judged on a scale of 100 for completion, correctness, clean code and documentation.

Tasks 1 & 2 are mandatory. Implementing task 3 is not a requirement. If completed, you will be awarded bonus points. We will also award bonus points for any extra justifiable considerations/improvements added to the application.

Your final score determines whether we will proceed to the next round of the interview.


## Tasks Background

The product designer has just shared some mockups with us. On the mockup, the user is able generate receipts for a given transaction. Due to regulatory requirements, our system needs to generate and save 10 different PDF copies of receipts each time the user clicks on the button to generate receipt for the transaction. Ideally, the receipts would all look different. But for the sake of this test, you can write a very simple receipt template that can be used for all of the 10 receipt generation operations.

At the very least, the receipt should contain: Name, Address, Phone Number and Total Amount Payable.


## Task 1

Build a receipt generation system that **conveniently** allows users to generate the receipts PDF. Please bear in mind that the system is not expected to return the receipts to the frontend. They can be saved in any medium you deem fit.


## Task 2

Expose the system to the public via an API endpoint such that the frontend application can call it with the necessary details and the receipts will be generated. However, we must ensure that only authenticated and authorized users are able to generate these receipts.

## Task 3 (Bonus)

Implement an interactive UI with which we can play with the API. 

Hint: Swagger UI is perfect. A React or Vue app hosted on Vercel or Netlify is also fine.


## ACCEPTANCE CRITERIA:
- The solution is available on either Github or Gitlab. Please add the following GitHub account as a maintainer: @simone-dexter if using GitHub

- Appropriate API documentation is added to the project

- API is deployed to Heroku (or a cloud hosting equivalent)

All the best!
