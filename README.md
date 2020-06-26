# Production Environment

In this project I have built a CI/CD pipeline for a microservices application for different deployment strategies. This is my proposal of capstone project of the Udacity Cloud DevOps Nanodegree Program.

## What I learnt, what I'm most proud of and which problems I had
## 1. Installation
## 2. Usage
## 3. Contributing
## 4. How it was developed
### a. Requirement steps
### b. Roadmap
### c. Rubric


---------------

### b. Roadmap

1. Choose a github repo.

- [x] Choose an app to lint. It is choosen a simple python app.
- [x] With a dockerfile

2. Jenkins 
- [X] Tried on an EC2 and discovered the benefits of Jenkins X. Setup the repo for continuous integration.
- [x] Test pipeline: photo of a failing linting. 

3. EKS. 
- [x] Create a cluster: photo that it works manually
- [x] Instances name rolling deployment
- [x] The deployment works.

## Motivation: What I learnt, what I'm most proud of and which problems I had

I've done software projects in hackathons or just project during college. I've realized that implementing automating pipelines for continuous integration and continuous deplyoment guarantees a quality of the software product that cannot be provided by manually assessing this quality. So, the aim of this project is fitting [the rubric of the capstone project](https://review.udacity.com/#!/rubrics/2577/view), with the final objective of creates a code that allows to easily automates this integration and deployment of a software repo in github. In general, a software is been identified to propose a certain ***value***. Then automating piepline should be provided (see image). Looking at the big picture, this repo includes the files of jenkins x + the pipeline overrided.

![software product pipeline big picture](https://github.com/chanakaudaya/solutions-architecture-patterns/blob/master/vendor-neutral/images/Enterprise-CICD-Pattern.png)

Big picture from https://github.com/chanakaudaya/solutions-architecture-patterns.

Under the hood this three componentes are managed by jenkins X:

1- A ***jenkinsfile => now buildpacks***. THere are many tools for implementing pipelines (as Jenkins, Travis CI, Circle CI, Gitlab. . .) In this repo it is proposed a jenkinsfile running in an ec2 instance. After setting an ec2 with jenkins, it is deployed Jenkins X. It is realized it offers certain better cabailities as gitops and this bukernetes orientation using helm charts. So, it is configure some Jenkins X environments, following their decoumentation architecture

![Jenkins X](https://jenkins-x.io/images/jx-arch.png)

In this sample it is proposed a pipeline aproximate to this one:

Install -> lint -> test -> Rolling deployments (on certain environments)

2- A ***description file*** for k8: as the software product is structured in microservices, docker is used to conteinarized the different services, and so the development, testing and production environment can be proposed on a kubernetes cluster.

3- ***AWS***: to adapat the demand, certain cloud services are used.

### What I learnt

I discovered how to automate quality assurance, with so much help of the differnet referneces i found (see references)

### What I'm most proud of

The easy way was to use Jenkins, but I decided to use the tool that is started to been used ritgh now, Jenkins X

### What problem I had

I had many problems, I was the entire week dealing with them, while I was learning. I highlight 5:

1. The first one was realizing that the arquitecture that Jenkisn X proposed was most automated in contnouos delivery than with Jenkins. As the Kuberntes deployments I will have to them on my own. So make decide if it was worth it trying Jnekins X or doing it in with Jenkins, wiht more documentation and help inthe last option. BUt I decided teh first, to try to innovate.
2. Then, I discovered there was two ways of installing Jenkins X, but the one in which the pipeline works was the one that does not inlcude a blue ocean dashboard but a CLI one.
3. THen, I had to learn which is the differnece between a Jenkins and a Jenkins X pipeline. Doing this I deployed so many cluster that my AWS cost raised up to 17&
4. Them, I discovered which are the benefits of helm and skaffold
5. But I was only able to do an audit as the lint didn't work for me.


-------------------

## 1. Installation

For setting this pipeline I:

First, download jenkins x form it official repo.

Then I created a cluster

For eks or gke

```
jx create cluster eks --skip-installation
jx create cluster gke --cluster-name xxxxx --skip-installation
```

It is initialize jenkins x with a jx-requirements.

```
jx boot -r  jx-requirements.yml
```

Then, it is initialized this app:

```
jx create quickstart --git-public
```

And choose python-http

Then is check that the environments work and than the application is running. It is create a quickstart sample, then put a photo of the activities to see thei

```
jx get activities
jx get application
```


## 2. Usage

When modified anything in the repo, a deplyoment is created.
 


## 3. Contributing
## 4. How it was developed

### a. Requirement steps

#### Step 1: Propose and Scope the Project
Plan what your pipeline will look like.

***Install -> lint -> test -> Rolling deployments (on certain environments)***

Decide which options you will include in your Continuous Integration phase.
Use Jenkins.


```
buildPack: python
pipelineConfig:
 pipelines:
  release:
   build:
    steps:
    - sh: pip install --upgrade pip
      name: upgrade
    - sh: pip install -r requirements.txt
      name: install
    - sh: pylint --disable=R,C,W1203 app.py
      name: lint
```


Pick a deployment type - either rolling deployment or blue/green deployment.

For the Docker application you can either use an application which you come up with, or use an open-source application pulled from the Internet, or if you have no idea, you can use an Nginx “Hello World, my name is (student name)” application.


#### Step 2: Use Jenkins, and implement blue/green or rolling deployment.

Create your Jenkins master box with either Jenkins and install the plugins you will need.

Set up your environment to which you will deploy code.

It is taken advantage of the [rolling updates](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) native of kubernetes deplyoments, to implement a rolling deplyoment. It is checked that the versions of the pod, are rolling when promote a change. So first, it is promoted a version 1, and then access witha  curl it is cehcked that it is a progressive cahgne between them.

#### Step 3: Pick AWS Kubernetes as a Service, or build your own Kubernetes cluster.
Use Ansible or CloudFormation to build your “infrastructure”; i.e., the Kubernetes Cluster.

***First, it is tried with [this cluster](!https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html). Note that, to manage eks form cloud9 [these steps](!https://eksworkshop.com/prerequisites/k8stools/) should be followed. Basically adding the administrationaccess role instead of teh eks related to the ec2***

It should create the EC2 instances (if you are building your own), set the correct networking settings, and deploy software to these instances.

As a final step, the Kubernetes cluster will need to be initialized. The Kubernetes cluster initialization can either be done by hand, or with Ansible/Cloudformation at the student’s discretion.


#### Step 4: Build your pipeline

Construct your pipeline in your GitHub repository.

Set up all the steps that your pipeline will include.

Configure a deployment pipeline.

Include your Dockerfile/source code in the Git repository.

Include with your Linting step both a failed Linting screenshot and a successful 

Linting screenshot to show the Linter working properly.

***After creating the qucikstart applcaition is copy and modified, and then applied:***

```
jx import
```

#### Step 5: Test your pipeline

Perform builds on your pipeline.

Verify that your pipeline works as you designed it.

*** Then using helm chart is deployed the service **

Take a screenshot of the Jenkins pipeline showing deployment and a screenshot of your AWS EC2 page showing the newly created (for blue/green) or modified (for rolling) instances. Make sure you name your instances differently between blue and green deployments.

### c. Rubric

#### Set up pipeline

- [x] ***Create Github repository with project code:*** All project code is stored in a GitHub repository and a link to the repository has been provided for reviewers.

These are the repos of the three other environments:

https://github.com/ablazleon/environment-jxgke6-staging
https://github.com/ablazleon/environment-jxgke6-production
https://github.com/ablazleon/environment-jxgke6-dev

- [ ] ***Use image repository to store Docker images*** The project uses a centralized image repository to manage images built in the project. After a clean build, images are pushed to the repository.

Yes, I set this images in gcr to public:

https://gcr.io/envjenkinsk8udacitycapstone/mynodejsjx

#### Build Docker Container


- [x] ***Execute linting step in code pipeline:*** Code is checked against a linter as part of a Continuous Integration step (demonstrated w/ two screenshots).

What I do is override [the pipeline.yml](https://github.com/jenkins-x-buildpacks/jenkins-x-kubernetes/blob/master/packs/python/pipeline.yaml), with the desire steps in jenkins-x.yml on the repo. 

- [x] ***Build a Docker container in a pipeline*** The project takes a Dockerfile and creates a Docker container in the pipeline.

In this last inherited pipeline, the docker container is automaticallty created.


#### Successful Deployment


- [x] ***The Docker container is deployed to a Kubernetes cluster:*** The cluster is deployed with CloudFormation or Ansible. This should be in the source code of the student’s submission.

Jenkins X deploy a kuberntes cluster, using cloud formation under the hood. I fisrt deploy  it on eks, but then switched to gke, as I ran teh eks cluster a couple days and it costs me 17$, when I have 100$ first credits in gke.

- [x] ***Use Blue/Green Deployment or a Rolling Deployment successfully*** The project performs the correct steps to do a blue/green or a rolling deployment into the environment selected. Student demonstrates the successful completion of chosen deployment methodology with screenshots.

As it can be seen in the images of ```jx promote``` after the application is tested that works on the dev environment is promote to production. Then, it can be seen that with   
```kubectl get po```, that images updated in a rolling fashion


#### Bonus

- [ ] Perform additional CI steps in the pipeline outside of just linting: ***as i have integrated jenkins X is easier to include additional CI steps than with the initial Jenkins that I setup, beacuse of the jenkins X buils packs***
