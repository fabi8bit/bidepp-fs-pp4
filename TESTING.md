# Bidepp - Testing



[Visit Bidepp](https://bidepp-cc1716a9edf6.herokuapp.com/)

---

I employed Google's Developer Tools to verify the proper functioning of all elements of the website and to guarantee the responsiveness across an array of screen sizes and devices. Furthermore, I conducted manual testing on the functionality to ensure a flawless user experience.

---

## Validation Testing

### HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site.

| Page | Result | Evidence |
| :--- | :--- | :---: |
| Home Page | Pass| [Home Page Validation]() |
| Blog Page | Pass | [Privacy Page Validation]() |
| Hotels | Pass | [Terms & Conditions Page Validation]() |
| Register | Pass | [Delivery Page Validation]() |
| Contact Form Page | Pass | [Contact Form Page Validation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fcontact%2F)|
| Log in| Pass | [Contact Success Page Validation](documentation/testing/validation/html/contact-success-validation.png) |
| Manage | Pass |[Product Page Validation](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fseaside-sewing.herokuapp.com%2Fproducts%2F%3Fcategory%3Dby_the_metre) |


### CSS

[W3C CSS](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.

| File | Result | Evidence |
| :--- | :--- | :---: |
| static/css/style.css | Pass | [static/css/style.css validation](documentation/testing/validation/css/base-validation.png) |


### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File | Result | Evidence |
| :--- | :--- | :---: |
| static/js/js/maps.js | Pass | [maps.js](documentation/testing/validation/js/checkout-stripe-elements-validation.png) |
| static/js/js/script.js  | Pass |[script.js](documentation/testing/validation/js/profiles-countryfield-validation.png) |

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python.

| File | Result | Evidence |
| :--- | :--- | :---: |
| **BIDEPP** |
| settings.py | Pass | [settings.py validation](documentation/testing/validation/python/settings-validation.png) |
| urls.py | Pass | [urls.py validation](documentation/testing/validation/python/seaside_sewing-urls-validation.png) |
| **BLOG** |
| forms.py | Pass | [apps.py validation](documentation/testing/validation/python/bag-apps-validation.png) |
| models.py | Pass | [contexts.py validation](documentation/testing/validation/python/bag-contexts-validation.png) |
| urls.py | Pass | [urls.py validation](documentation/testing/validation/python/bag-urls-validation.png) |
| views.py | Pass | [views.py validation](documentation/testing/validation/python/bag-views-validation.png) |

### Lighthouse
#### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Desktop Lighthouse Testing](documentation/testing/lighthouse/home-desk-lh-val.png) |
| Reviews | ![Reviews Desktop Lighthouse Testing](documentation/testing/lighthouse/products-desk-lh-val.png) |
| Hotels | ![Hotels Detail Desktop Lighthouse Testing](documentation/testing/lighthouse/product-detail-desk-lh-val.png) |
| Login | ![Login Desktop Lighthouse Testing](documentation/testing/lighthouse/add-product-desk-lh-val.png) |
| Register | ![Register Desktop Lighthouse Testing](documentation/testing/lighthouse/edit-product-desk-lh-val.png) |
| Manage | ![Manage Desktop Lighthouse Testing](documentation/testing/lighthouse/bag-desk-lh-val.png) |

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Mobile Lighthouse Testing](documentation/testing/lighthouse/home-desk-lh-val.png) |
| Reviews | ![Reviews Mobile Lighthouse Testing](documentation/testing/lighthouse/products-desk-lh-val.png) |
| Hotels | ![Hotels Mobile Lighthouse Testing](documentation/testing/lighthouse/product-detail-desk-lh-val.png) |
| Login | ![Login Mobile Lighthouse Testing](documentation/testing/lighthouse/add-product-desk-lh-val.png) |
| Register | ![Register Mobile Lighthouse Testing](documentation/testing/lighthouse/edit-product-desk-lh-val.png) |
| Manage | ![Manage Mobile Lighthouse Testing](documentation/testing/lighthouse/bag-desk-lh-val.png) |

### Wave

[wave](https://wave.webaim.org/)

| Page | Errors |
| :--- | :--- |
| Home Page | No errors|
| Reviews | No errors |
| Hotels | No errors |
| Login | No errors |
| Register | No errors |
| Manage | No errors |

## Automated Testing

I didn't run any automated test.

## Manual Testing
The site was tested in all the parts and working as expected

#### Sign-in, Sign-up, Logout 
- Working as expected


#### Clear comment form after submitting:
- It was achieved by moving the endif template tag before the form in the review_detail.html

#### Managing Panel
- The Review and Hotel managing panel, at this stage, is able to display only the Published review and the Hotels associated with it (all the reviews and hotels are accessible from the admin page). In order to retrieve the data for all the reviews (draft and published), I decided to use the same class as for the blog. A possible solution is to duplicate the class and delete the filter in order to display both the draft and published reviews.

- Hotels are only visible when associated to a review because it's a blog reviewing Hotels and not an Hotels directory.

- The slug field in the new Review form is not generating automaticaly and has to be typed in. In the Django admin page It's fully automatic. A possible solution could be implementing a javascript function. I found an interesting solution at [this link](https://gist.github.com/codeguy/6684588) or [this link](https://stackoverflow.com/questions/12098319/how-add-a-pre-populated-field-to-a-form-submission-in-django-like-in-admin)

- Deleting Reviews and Hotels was not working until I moved the order of the urls path. I researched around but didn't understand the logic.
[Here](https://stackoverflow.com/questions/36429144/page-not-found-404-no-post-matches-the-given-query) I found a possible explanation.

#### Map displaying
- In order to display the map for the hotels, I had to pass data from the database to the map.js using tag template. That was achieved after reading [this post](https://stackoverflow.com/questions/28516101/django-how-to-pass-template-variable-to-javascript-onclick-routine)

## Bugs
- The counter of the like button is miss alligned. I tried to solve it adding a class called no-gutters but at this stage seems not to solve it. The bug is unresolved

- During the lighthouse test I discovered an issue with the map.js script. As long as the variables for this function to operate are passed from one of the templates, at the moment of the loading those variables are not declared. At the moment this issue is not resolved but a possible solution is to initialize the variables on a separate file.






