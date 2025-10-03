# TemporaryRepository
The Repository for when I need a public repository for random submissions :P


Before Reading further, it is important to note that the docs submitted in Part 1 also contains a section for Part 2, which is written in a much better way, and also has ✨illustrations✨ (aka, stuff I drew on Google Draw to have the document look more presentable). The Link to the docs is : https://docs.google.com/document/d/1t29mKwR09C4uYoYCNeoLOIn8kN0CyTWs8LTR-8Mf0X0/edit?usp=sharing

In this repository, there is also an included code file in which I tried (and failed horribly, as shown by the multiple errors you might get while running the file) to implement the code. I used IBM's Qiskit to implement the quantum gates, and for learning how to use Qiskit, I used the Qiskit implementation pages provided by IBM, and as a result, the final code turned out very similar, mainly due to the many failed attempts at trying to give it my own version.



Now, starting with the thoughts as to how to implement a circuit to differentiate a constant and a balanced function.
  I first started by noticing that there was a pattern in every circuit I saw, which was they always used a Hadamard gate between two qubits at the start in almost every algorithm. Then, as shown in the FreeCodeCamp video, I started with the standard circuit, of Hadmard, Function, then Hadamard. This worked out for a single gate, and after doing a little more research (Watching further into the video) I saw that this was called the Deutsch algorithm, and it worked on the principle of Phase Kickback.
  After this, I thought that Deutsch algorithm solved the exact problem that I was given, which was finding out if the Crystalline box gave perfectly balanced outputs or was just a constant function outputter. Then, similar to Deutsch algorithm, (or I guess identically since nothing was added), I solved for the state |𝜓⟩ at 1,2,3 and output.
    Here, I got confused on how to solve further for the Hadamard Gate and get the answer. Then I found a way to think of x as x₁x₂x₃, and then apply the Hadamard Gate separately.So what was found, was that in fact this model worked. If the function f was balanced, then the measured result would be anything other than the |000⟩ state, But if the function was constant, then the measured state would definitely be the |000⟩ state. Then I actually looked forward in the video, which I had used for help in some of the Math, and found that this was the exact result used, and this algorithm was called the Deutch-Jozsa Algorithm.
  While the algorithm is solved for the general case of n-qubits, for our case, we would use the n=3 case, giving the exact same result. Now that this was done, I decided to write a Code using Quiskit to represent this.



  This Section concerns the coding section of the Problem Statement. The Quantum circuit can be shown as three input qubits, as well as a single ancellary qubit being acted upon by a Hadamard Gate, before being inputted into a Oracle U. Then the oracle outputs the first three input qubits, and applies another set of Hadamard gates on it before measuring all three input qubits. 
  The idea was to apply this in a coding platform. I thought it would be simple. I was stupid. I started by defining a function that had two ways, one in which you could either choose to input the function yourself or have it automatically made. The automatically made had an equal probability of being either perfectly balanced, or fully constant, with both 0 filled or 1 filled. Then when I tried to integrate it into the rest of my circuit, I could not understand how to have every index of the function act on the states one by one. So I opened the quiskit implementation page on IBM, and realised I did everything wrong and that I needed to delete everything and start again.
  I then consulted the IBM Quiskit implementation pages and created a new oracle, Then defined a CircuitMaker, created the Hadamard,Then Oracle, Then Hadamard Circuit. Then I defined the Result Giver Function which would compute the resulting string and output if the function was balanced or constant.

  I believe it is important to note that all this (Both the code as well as the initial answers for Section 1) was written in Notepad since I did not have enough space in my laptop for an IDE, so there might be many errors. Please don't bully me because of the hundreds of errors that would be present, and look at the logic instead.
   
   Thank You.
   
   Please see the attached code file (I went thru a lot of pain for it) Also the first large part of commented code is the code I had initially written for the Automatic production of function, but then realised was broken, and didnt have the heart to delete. Ignore it if it bothers you, read it if you find it interesting, even though there is nothing interesting about it.
