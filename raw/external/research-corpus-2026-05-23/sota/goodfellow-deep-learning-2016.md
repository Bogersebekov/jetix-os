---
title: goodfellow-deep-learning-2016
source_pdf: goodfellow-deep-learning-2016.pdf
source_folder: sota
extraction_method: tesseract-ocr-psm6-oem1-100dpi
extraction_date: 2026-05-24
pages_total: 972
pages_ocr: 25
ocr_coverage: partial
ocr_remaining: 947
chars: 22057
approx_tokens: 5514
ocr_runtime_sec: 14.5
pipeline_phase: 3-ocr-extracted
constitutional_posture: R1-surface
note: PARTIAL OCR — first 25 pages only. 947 pages flagged for paid OCR re-processing.
---

## Page 1

AD ka) fg BME NN G44 a) RA.
UB Vai aay an ae le PLES TIS
(VF DEEP LEARNING 28
VE : ae
ag, 7 Aan Goodfellow, Yoshua Bengio, - a
6 ke and Aaron Courville a3 é
Va ae ASR A =
we A \ Nh aS aay gn, Cane = Dyes
WS ANE AI a
©. Cs Se ee ee HY} Meee s Ley Gx Mek Asa
NSLS aan Ni TER Se Hh bee Y
Pay, Rae at “a ‘Sst pee ee oe } nd Be
Z ye \\ ‘ee sige oo Miah f
Pe SY NN ORR eA paN:
PE a eae 7 atl te
x = cM of ea ur Waly “A
LN Tout ase eee “Gags ait wh ¢ bay"
Vicia ea a IR Tage Nat Re roe
Win Gee Pep Ney ROAM N ta ie
LAGE irs thay i: eee i OS Oe mee
3 tee Sa rae Toe sha
oP EN nes Ma, 24 Oe Ae ha eee cs rat atari
Copagtet seta OP Eas. ee
* ae ie a OS, \ ge is f Sic i nek Sa eee
ager) a Mahia ety eke yi Retr
HD pine ee Ar Ci ES ae AS ae
by heh 5 ae Ff pg oy kee Wee
a se Ve te At Sandee
Ned ‘Sea atest LP SEAS ge aS
i Gl OR ~ Ge ee Ne oe ES
et Nar Lenses > oy A VE eS
i eb Dar a eee ph OZ % 3
EMivip ser rg % ER ay S Ae ee Sess ae ie
E\ pers Dy ety Poy tre Kien ary Wea on oS er

## Page 2

HAIN SO TORE
Wi Oe AVA IPAE ke eran
PAA So) eee ee 28
) 44) A A) RNR Lee AAS X
(NW DEEP LEARNING £ a
li FP an Goodfellow, Yoshua Bengio, (ee
4g) and Aaron Courville nS me
Dir a Na Sai Ca
Pet A \ Sanh Ate a
BS IN kien
i NN Rs
ro Wena s
Tie AN er ae
UG iN ens SRN WR
st a ee a
Sa We ee Coe i
Be: ER Ny AN Wate ee
Ee RS te BO AE ROG Sea dg a pete
DN aS Ms paw et eae gages a eR
Oe” Ca te ma Ce ean SY BSD
ete alte gS Stitt SO AY
ae Fea e a OW we ee ret
sig ee te Nee = hee =e *
OE diac er a ee

AP PRES CINE Pog” Wg ee
Btn / tehle 7 Boe ay

i ‘G as EAS Bs esters

, x a & nee Pao Y 2

githe =

WN ss ARSE

OceanofPDF.com

## Page 3

Deep Learning
OceanofPDF.com

## Page 4

Adaptive Computation and Machine Learning
Thomas Dietterich, Editor
Christopher Bishop, David Heckerman, Michael Jordan, and Michael Kearns,
Associate Editors
A complete list of books published in The Adaptive Computation and
Machine Learning series appears at the back of this book.

OceanofPDF.com

## Page 5

Deep Learning
Ian Goodfellow
Yoshua Bengio and
Aaron Courville
The MIT Press
Cambridge, Massachusetts
London, England
OceanofPDF.com

## Page 6

© 2016 Massachusetts Institute of Technology
All rights reserved. No part of this book may be reproduced in any form by
any electronic or mechanical means (including photocopying, recording, ot
information storage and retrieval) without permission in writing from the
publisher.
This book was set in SFRM1095 by diacriTech, Chennai.
Library of Congress Cataloging-in-Publication Data
Names: Goodfellow, lan, author. | Bengio, Yoshua, author. | Courville, Aaron,
author.
Title: Deep learning / Tan Goodfellow, Yoshua Bengio, and Aaron Courville.
Description: Cambridge, MA : MIT Press, [2017] | Series: Adaptive
computation and machine learning series | Includes bibliographical
references and index.
Identifiers: LCCN 2016022992 | ISBN 978-0-262-33737-3
Subjects: LCSH: Machine learning,
Classification: LCC Q325.5 .G66 2017 | DDC 006.3/1-de23 LC record
available at https://Iccn.loc.gov/2016022992
d_r0
OceanofPDF.com

## Page 7

Contents
Copyright
Website
Acknowledgments
Notation
1 Introduction
1.1 | Who Should Read This Book?
1.2 Historical Trends in Deep Learning
I Applied Math and Machine Learning Basics
2 Linear Algebra
2.1 Scalars, Vectors, Matrices and Tensors
2.2 Multiplying Matrices and Vectors
2.3. Identity and Inverse Matrices
2.4 Linear Dependence and Span
2.5 Norms
2.6 Special Kinds of Matrices and Vectors
2.7 Eigendecomposition
2.8 Singular Value Decomposition
2.9 The Moore-Penrose Pseudoinverse
2.10 The Trace Operator

## Page 8

2.11 The Determinant
2.12 Example: Principal Components Analysis
3 Probability and Information Theory
3.1 Why Probability?
3.2 Random Variables
3.3 Probability Distributions
3.4 Marginal Probability
3.5 Conditional Probability
3.6 The Chain Rule of Conditional Probabilities
3.7 Independence and Conditional Independence
3.8 Expectation, Variance and Covariance
3.9 Common Probability Distributions
3.10 Useful Properties of Common Functions
3.11 Bayes’ Rule
3.12 Technical Details of Continuous Variables
3.13 Information Theory
3.14 Structured Probabilistic Models
4 Numerical Computation
4.1 Overflow and Underflow
4.2 Poor Conditioning
4.3 Gradient-Based Optimization
44 — Constrained Optimization
4.5 Example: Linear Least Squares
5 Machine Learning Basics
5.1 Learning Algorithms
5.2 Capacity, Overfitting and Underfitting
5.3 Hyperparameters and Validation Sets
5.4 Estimators, Bias and Variance

## Page 9

5.5 Maximum Likelihood Estimation
5.6 Bayesian Statistics
5.7 Supervised Learning Algorithms
5.8 Unsupervised Learning Algorithms
5.9 Stochastic Gradient Descent
5.10 Building a Machine Learning Algorithm
5.11 Challenges Motivating Deep Learning
Il Deep Networks: Modern Practices
6 Deep Feedforward Networks
6.1 Example: Learning XOR
6.2 Gradient-Based Learning
6.3 Hidden Units
6.4 Architecture Design
6.5 Back-Propagation and Other Differentiation Algorithms
6.6 Historical Notes
7 Regularization for Deep Learning
7.1 Parameter Norm Penalties
7.2. Norm Penalties as Constrained Optimization
7.3. Regularization and Under-Constrained Problems
7.4 Dataset Augmentation
7.5 Noise Robustness
7.6  Semi-Supervised Learning
7.7 Multitask Learning
7.8 Early Stopping
7.9 Parameter Tying and Parameter Sharing
7.10 Sparse Representations
7.11 Bagging and Other Ensemble Methods

## Page 10

7.12 Dropout

7.13. Adversarial Training

7.14 Tangent Distance, Tangent Prop and Manifold Tangent Classifier
8 Optimization for Training Deep Models

8.1 How Learning Differs from Pure Optimization

8.2 Challenges in Neural Network Optimization

8.3. Basic Algorithms

8.4 Parameter Initialization Strategies

8.5 Algorithms with Adaptive Learning Rates

8.6 Approximate Second-Order Methods

8.7 Optimization Strategies and Meta-Algorithms
9 Convolutional Networks

9.1 The Convolution Operation

9.2 Motivation

9.3 Pooling

9.4 Convolution and Pooling as an Infinitely Strong Prior

9.5 Variants of the Basic Convolution Function

9.6 Structured Outputs

9.7 Data Types

9.8 Efficient Convolution Algorithms

9.9 Random or Unsupervised Features

9.10 The Neuroscientific Basis for Convolutional Networks

9.11 Convolutional Networks and the History of Deep Learning
10 Sequence Modeling: Recurrent and Recursive Nets

10.1 Unfolding Computational Graphs

10.2 Recurrent Neural Networks

10.3. Bidirectional RNNs

10.4 Encoder-Decoder Sequence-to-Sequence Architectures

## Page 11

10.5 Deep Recurrent Networks
10.6 Recursive Neural Networks
10.7. The Challenge of Long-Term Dependencies
10.8 Echo State Networks
10.9 Leaky Units and Other Strategies for Multiple Time Scales
10.10 The Long Short-Term Memory and Other Gated RNNs
10.11 Optimization for Long-Term Dependencies
10.12 Explicit Memory
11 Practical Methodology
11.1 Performance Metrics
11.2. Default Baseline Models
11.3. Determining Whether to Gather More Data
11.4 Selecting Hyperparameters
11.5 Debugging Strategies
11.6 Example: Multi-Digit Number Recognition
12 Applications
12.1 Large-Scale Deep Learning
12.2 Computer Vision
12.3 Speech Recognition
12.4 Natural Language Processing
12.5 Other Applications
Ill Deep Learning Research
13 Linear Factor Models
13.1 Probabilistic PCA and Factor Analysis
13.2. Independent Component Analysis (ICA)
13.3. Slow Feature Analysis
13.4 Sparse Coding

## Page 12

13.5 Manifold Interpretation of PCA
14 Autoencoders

14.1 Undercomplete Autoencoders

14.2, Regularized Autoencoders

14,3. Representational Power, Layer Size and Depth

14.4 Stochastic Encoders and Decoders

14.5 Denoising Autoencoders

14.6 Learning Manifolds with Autoencoders

14.7 Contractive Autoencoders

14.8 Predictive Sparse Decomposition

14.9 Applications of Autoencoders
15. Representation Learning

15.1 Greedy Layer-Wise Unsupervised Pretraining

15.2. Transfer Learning and Domain Adaptation

15.3. Semi-Supervised Disentangling of Causal Factors

15.4 Distributed Representation

15.5 Exponential Gains from Depth

15.6 Providing Clues to Discover Underlying Causes
16 Structured Probabilistic Models for Deep Learning

16.1 The Challenge of Unstructured Modeling

16.2. Using Graphs to Describe Model Structure

16.3 Sampling from Graphical Models

16.4 Advantages of Structured Modeling

16.5 Learning about Dependencies

16.6. Inference and Approximate Inference

16.7 The Deep Learning Approach to Structured Probabilistic Models
17 Monte Carlo Methods

## Page 13

17.1 Sampling and Monte Carlo Methods
17.2, Importance Sampling
17.3. Markov Chain Monte Carlo Methods
17.4. Gibbs Sampling
17.5 The Challenge of Mixing between Separated Modes
18 Confronting the Partition Function
18.1 The Log-Likelihood Gradient
18.2 Stochastic Maximum Likelihood and Contrastive Divergence
18.3 Pseudolikelihood
18.4 Score Matching and Ratio Matching
18.5 Denoising Score Matching
18.6 Noise-Contrastive Estimation
18.7 Estimating the Partition Function
19 Approximate Inference
19.1. Inference as Optimization
19.2 Expectation Maximization
19.3. MAP Inference and Sparse Coding
19.4 Variational Inference and Learning
19.5 Learned Approximate Inference
20 Deep Generative Models
20.1 Boltzmann Machines
20.2 Restricted Boltzmann Machines
20.3 Deep Belief Networks
20.4 Deep Boltzmann Machines
20.5 Boltzmann Machines for Real-Valued Data
20.6 Convolutional Boltzmann Machines
20.7 Boltzmann Machines for Structured or Sequential Outputs
20.8 Other Boltzmann Machines

## Page 14

20.9 Back-Propagation through Random Operations
20.10 Directed Generative Nets
20.11 Drawing Samples from Autoencoders
20.12 Generative Stochastic Networks
20.13 Other Generation Schemes
20.14 Evaluating Generative Models
20.15 Conclusion
Bibliography
Index
OceanofPDF.com

## Page 15

Website
www.deeplearningbook.org
‘This book is accompanied by the above website. The website provides a variety
of supplementary material, including exercises, lecture slides, corrections of
mistakes, and other resources that should be useful to both readers and
instructors.
OceanofPDF.com

## Page 16

Acknowledgments
This book would not have been possible without the contributions of many
people.

We would like to thank those who commented on our proposal for the
book and helped plan its contents and organization: Guillaume Alain,
Kyunghyun Cho, Gaglar Giilgehre, David Krueger, Hugo Larochelle, Razvan
Pascanu and Thomas Rohée.

We would like to thank the people who offered feedback on the content of
the book itself, Some offered feedback on many chapters: Martin Abadi, Ishaq
Aden-Ali, Guillaume Alain, Ion Androutsopoulos, Laura Ball, Fred Bertsch,
Olexa Bilaniuk, Ufuk Can Bigici, Matko BoSnjak, John Boersma, Francois
Brault, Greg Brockman, Alexandre de Brébisson, Pierre Luc Carrier, Sarath
Chandar, Pawel Chilinski, Mark Daoust, Oleg Dashevskii, Laurent Dinh,
Stephan Dreseitl, Gudmundur Einarsson, Hannes von Essen, Jim Fan, Miao
Fan, Meire Fortunato, Frédéric Francis, Nando de Freitas, Gaglar Giilgehre,
Jurgen Van Gael, Yaroslav Ganin, Javier Alonso Garcia, Aydin Gerek, Stefan
Heil, Jonathan Hunt, Gopi Jeyaram, Hreinn Juliusson, Chingiz Kabytayev,
Lukasz Kaiser, Varun Kanade, Asifullah Khan, Akiel Khan, John King,
Diederik P. Kingma, Dominik Laupheimer, Yann LeCun, Marcin Lebiedé,
Minh Lé, Max Marion, Rudolf Mathey, Matias Mattamala, Abhinav Maurya,
Vincent Michalski, Kevin Murphy, Oleg Miirk, Hung Ngo, Roman Novak,
Augustus Q. Odena, Simon Pavlik, Karl Pichotta, Eddie Pierce, Kari Pulli,
Roussel Rahman, Tapani Raiko, Anurag Ranjan, Johannes Roith, Mihaela
Rosca, Halis Sak, César Salgado, Grigory Sapunov, Yoshinori Sasaki, Mike
Schuster, Julian Serban, Nir Shabat, Ken Shirriff, Andre Simpelo, Scott
Stanley, David Sussillo, Ilya Sutskever, Carles Gelada Sée2, Graham Taylor,
Valentin Tolmer, Massimiliano Tomassoli, An Tran, Shubhendu Trivedi, Alexey
Umnov, Vincent Vanhoucke, Robert Viragh, Marco Visentini-Scarzanella,

## Page 17

Martin Vita, David Warde-Farley, Dustin Webb, Shan-Conrad Wolf, Kelvin
Xu, Wei Xue, Ke Yang, Li Yao, Zygmunt Zajac and Ozan Gaglayan.

We would also like to thank those who provided us with useful feedback on
individual chapters:

+ Notation: Zhang Yuanhang.

* Chapter 1, Introduction: Yusuf Akgul, Sebastien Bratieres, Samira
Ebrahimi, Charlie Gorichanaz, Benned Hedegaard, Brendan
Loudermilk, Petros Maniatis, Eric Morris, Cosmin Parvulescu,
Muriel Rambeloarison, Alfredo Solano, Timothy Whelan and Ersin
Gine.

+ Chapter 2, Linear Algebra: Amjad Almahairi, Nikola Banié, Kevin
Bennett, Philippe Castonguay, Oscar Chang, Eric Fosler-Lussier,
Andrey Khalyavin, Sergey Oreshkoy, Istvan Petrds, Dennis Prangle,
Thomas Rohée, Gitanjali Gulve Sehgal, Colby Toland, Alessandro
Vitale and Bob Welland.

+ Chapter 3, Probability and Information Theory: John Philip
Anderson, Kai Arulkumaran, Ana-Maria Cretu, Vincent Dumoulin,
Rui Fa, Stephan Gouws, Artem Oboturoy, Patrick Pan, Antti
Rasmus, Alexey Surkov and Volker Tresp.

* Chapter 4, Numerical Computation: Tran Lam An, Tomasz
Dryjanski, Ian Fischer, William Gandler, Mahendra Kariya and Hu
Yuhuang.

+ Chapter 5, Machine Learning Basics: Dzmitry Bahdanau, Mark
Cramer, Eric Dolores, Justin Domingue, Ron Fedkiw, Nikhil Garg,
Guillaume de Laboulaye, Jon McKay, Makoto Otsuka, Bob Pepin,
Philip Popien, Klaus Radke, Emmanuel Rayner, Adam Réiycki, Eric
Sabo, Imran Saleh, Peter Shepard, Kee-Bong Song, Zheng Sun,
Alexandre Torres and Andy Wu.

+ Chapter 6, Deep Feedforward Networks: Uriel Berdugo, Fabrizio
Bottarel, Elizabeth Burl, Ishan Durugkar, Jeff Hlywa, Jong Wook
Kim, David Krueger, Ilya Kulakov and Aditya Kumar Praharaj.

* Chapter 7, Regularization for Deep Learning: Brian Bartoldson,
Morten Kolbek, Kshitij Lauria, Inkyu Lee, Sunil Mohan, Hai Phong

## Page 18

Phan and Joshua Salisbury.

+ Chapter 8, Optimization for Training Deep Models: Marcel
Ackermann, Tushar Agarwal, Peter Armitage, Rowel Atienza,
Andrew Brock, Max Hayden Chiz, Gregory Galperin, Aaron
Golden, Russell Howes, Hill Ma, Tegan Maharaj, James Martens,
Kashif Rasul, Thomas Stanley, Klaus Strobl, Nicholas Turner and
David Zhang.

+ Chapter 9, Convolutional Networks: Martin Arjovsky, Eugene
Brevdo, Jane Bromley, Konstantin Divilov, Eric Jensen, Mehdi
Mirza, Hanan Othman, Alex Paino, Guillaume Rochette, Marjorie
Sayer, Ryan Stout and Wentao Wu.

* Chapter 10, Sequence Modeling: Recurrent and Recursive Nets:
Gékgen Eraslan, Nasos Evangelou, Steven Hickson, Christoph
Kamann, Martin Krasser, Razvan Pascanu, Diogo Pernes, Ryan
Pilgrim, Lorenzo von Ritter, Rui Rodrigues, Dmitriy Serdyuk,
Dongyu Shi, Simon Walz, Kaiyu Yang and Ruiging Yin.

+ Chapter 11, Practical Methodology: Daniel Beckstein and Kenji
Kaneda.

+ Chapter 12, Applications: George Dahl, Vladimir Nekrasov and
Ribana Roscher.

* Chapter 13, Linear Factor Models: Jayanth Koushik.

+ Chapter 14, Autoencoders: Hassan Masum.

+ Chapter 15, Representation Learning: Kunal Ghosh, Rodney
Melchers, Will Morley and Mateo Torres-Ruiz.

* Chapter 16, Structured Probabilistic Models for Deep Learning:
Deng Qingyu, Harry Braviner, Timothy Cogan, Diego Marez,
Anton Varfolom and Victor Xie.

+ Chapter 18, Confronting the Partition Function: Sam Bowman and
Jin Kim.

+ Chapter 19, Approximate Inference: Yujia Bao.

+ Chapter 20, Deep Generative Models: Nicolas Chapados, Daniel
Galvez, Marc Katzef, Wenming Ma, Fady Medhat, Shakir Mohamed

## Page 19

and Grégoire Montavon.
+ Bibliography: Lukas Michelbacher, Leslie N. Smith and Max Xie.

We also want to thank those who allowed us to reproduce images, figures
or data from their publications. We indicate their contributions in the figure
captions throughout the text.

We would like to thank Lu Wang for writing pdf2htmlEX, which we used
to make the web version of the book, and for offering support to improve the
quality of the resulting HTML. We also thank Simon Lefrangois and Satya
Ortiz-Gagné for incorporating MIT Press’s edits to our manuscript back into
the web edition, and for helping incorporate reader feedback from the web.

We would like to thank Ian’s wife Daniela Flori Goodfellow for patiently
supporting Ian during the writing of the book as well as for help with
proofreading,

We would like to thank the Google Brain team for providing an intellectual
environment where Ian could devote a tremendous amount of time to writing
this book and receive feedback and guidance from colleagues. We would
especially like to thank Ian's former manager, Greg Corrado, and his current
manager, Samy Bengio, for their support of this project. Finally, we would like
to thank Geoffrey Hinton for encouragement when writing was difficult.

OceanofPDF.com

## Page 20

Notation
This section provides a concise reference describing the notation used
throughout this book. If you are unfamiliar with any of the corresponding
mathematical concepts, we describe most of these ideas in chapters 2-4.
Numbers and Arrays
a A scalar (integer or real)
a Avector
A Amatrix
A Atensor
Ty Identity matrix with n rows and n columns
I Identity matrix with dimensionality implied by context
e4) Standard basis vector [0, ... 0, 1,0, ..., 0] with a 1 at position i
diag(a) A square, diagonal matrix with diagonal entries given by @
a Ascalar random variable
a A vector-valued random variable
A A matrix-valued random variable
Sets and Graphs
A A set
R The set of real numbers

## Page 21

{0,1} The set containing 0 and 1
{0, 1, ..., 2} The set of all integers between 0 and n
[4 6] The real interval including a and
(a, 6] The real interval excluding a but including 5
A\B Set subtraction, i.e., the set containing the elements of A that
are not inB
G A graph
Pag(xi) — The parents of x; in
Indexing
4; Element i of vector a, with indexing starting at 1
aj Allelements of vector a except for element i
Ajj Element i, j of matrix A
Aj, Row i of matrix A
A; Column j of matrix A
Aik Element (i,j, #) of a 3-D tensor A
A..j 2-D slice of a 3-D tensor
aj Element i of the random vector a
Linear Algebra Operations
A’ Transpose of matrix A
At — Moore-Penrose pseudoinverse of A
AGB Element-wise (Hadamard) product of A and B
det(A) Determinant of A

## Page 22

Calculus

dy oe .
E Derivative of y with respect to x
ai
dy
Be Partial derivative of y with respect to x

Vig) Gradient of y with respect to x

Vw Matrix derivatives of y with respect to X

Vxy Tensor containing derivatives of y with respect to X
of
Bs Jacobian matrix J € R”"*” of f:R” + R™

V2f(@) or H(f(x) The Hessian matrix of fat input point x
/ f(w)dz Definite integral over the entire domain of x
f f(w)dx Definite integral with respect to x over the set S
Probability and Information Theory
aLb The random variables a and b are independent
alb|e They are conditionally independent given ¢
Pla) A probability disttibution over a disctete variable
fa) A probability distribution over a continuous variable, ot

p over a variable whose type has not been specified

a~P Random variable a has distribution P

Ex~p[f(#)] or Ef(©) Expectation of fx) with respect to P(x)
Var(fx)) Variance of fix) under P(x)
Cov(fx), g(x)) — Covariance of fix) and g(x) under P(x)
Hs) Shannon entropy of the random variable x

## Page 23

DKLAQ —_Kullback-Leibler divergence of P and Q
Nain.) Gaussian distribution over x with mean g and covariance
Functions
f:A—B The function fwith domain A and range B
fog Composition of the functions fand g
A function of x paramettized by 8. (Sometimes we write Aix)
fix 9) , . ,
and omit the argument 0 to lighten notation)
logx Natural logarithm of x
—
OC) Logistic sigmoid, 1 + exp(—=)
Sx) Sofeplus, log(1 + exp(x))
lly IP norm of x
ied L? norm of x
at Positive part of x, ive., max(0, x)
[condition is 1 if the condition is true, 0 otherwise
Sometimes we use a function f whose argument is a scalar but apply it to a
vector, matrix, or tensor: fx), UX), o AX). This denotes the application of fto
the array element-wise. For example, if C = o(X), then Cj,j,¢ = 0(%j,,4) forall
valid values of i, j and &.
Datasets and Distributions
Pdata The data generating distribution
Pasta ‘The empirical distribution defined by the training set
X Asset of training examples

## Page 24

x) The #th example (input) from a dataset
9 ory The target associated with x for supervised learning
X The mx n matrix with input example x in row X;,;
OceanofPDF.com

## Page 25

1

Introduction

Inventors have long dreamed of creating machines that think. This desire dates
back to at least the time of ancient Greece. The mythical figures Pygmalion,
Daedalus, and Hephaestus may all be interpreted as legendary inventors, and
Galatea, Talos, and Pandora may all be regarded as artificial life (Ovid and
Martin, 2004; Sparkes, 1996; Tandy, 1997).

When programmable computers were first conceived, people wondered
whether such machines might become intelligent, over a hundred years before
one was built (Lovelace, 1842). Today, artificial intelligence (Al) is a thriving
field with many practical applications and active research topics, We look to
intelligent software to automate routine labor, understand speech or images,
make diagnoses in medicine and support basic scientific research.

In the early days of artificial intelligence, the field rapidly tackled and
solved problems that are intellectually difficult for human beings but relatively
seraightforward for computers—problems that can be described by a list of
formal, mathematical rules, The true challenge to artificial intelligence proved
to be solving the tasks that are easy for people to perform but hard for people
to describe formally—problems that we solve intuitively, that feel automatic,
like recognizing spoken words or faces in images.

This book is about a solution to these more intuitive problems. This
solution is to allow computers to learn from experience and understand the
world in terms of a hierarchy of concepts, with each concept defined through
its relation to simpler concepts. By gathering knowledge from experience, this
approach avoids the need for human operators to formally specify all the
knowledge that the computer needs. The hierarchy of concepts enables the