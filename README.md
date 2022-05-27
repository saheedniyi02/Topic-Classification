# Topic-Classification
This is a machine learning model deployed to a FastApi endpoint,
The model classifies a text and identifies the topic the text belongs to.
This model can be used by blog websites to classify blog posts and predict
the section/topic the blog should be posted

The model used is a count vectorizer+ naive Bayes (MultinomialNB) model.
The topics/sections are:
<ul><li>Politics</li>
<li>Religion</li>
<li>Sports</li>
<li>Literature</li>
<li>Computers</li>
<li>Art, Graphics & Video</li>
<li>Travel</li>
<li>Gaming</li>
<li>Education</li>
<li>Fashion</li>
<li>Business</li>
<li>Investment</li>
<li>TV/Movies</li>
<li>Phones</li>
<li>Romance</li>
<li>Career</li>
<li>Programming</li>
<li>Music/Radio</li>
<li>Webmasters</li></ul>

The data used was webscraped from Nairaland, Africa's largest discussion forum
