// Minh Nguyen
// Homework 4: F# Assignment 1 -- Learning Exercises
// All of the code you turn in must have been written by you without immediate 
// reference to another solution to the problem you are solving.  That means
// that you can look at other programs to see how someone solved a similar
// problem, but you shouldn't have any code written by someone else visible
// when you write yours

// q1
let rec maxCubeVolume l =
    match l with
    | [] -> 0.0
    | (a,b,c)::tl -> let vol = maxCubeVolume tl
                        in
                        if vol > (a*b*c)
                        then vol
                        else (a*b*c)

// q2
let rec findMatches letter = function
    | [] -> []
    | hd::tl -> if letter = fst(hd)
                        then List.sort (snd(hd)::findMatches letter tl)
                        else findMatches letter tl

// q3
// Tree definition for problem 3
type BST =
    | Empty
    | TreeNode of int * BST * BST

// insert function
let rec insert value tree =
    match tree with
        | Empty -> TreeNode(value, Empty, Empty)
        | TreeNode(curr, left, right) -> 
            if curr = value then tree
            else if curr > value then TreeNode(curr, (insert value left), right)
            else TreeNode(curr, left, (insert value right))

// contains function
let rec contains value tree =
    match tree with
        | Empty -> false
        | TreeNode(curr, left, right) ->
            if value < curr
                then contains value left
            else if value = curr
                then true
            else contains value right;;

// count function
let rec count func tree =
    match tree with
        | Empty -> 0
        | TreeNode(curr, left, right) ->
            if func curr
                then 1 + (count func left) + (count func right)
            else (count func left) + (count func right) 

// evenCount function
let rec evenCount tree =
    count (fun curr -> curr % 2 = 0) tree
