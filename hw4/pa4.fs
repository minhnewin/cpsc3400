/// Minh Nguyen
/// Homework 4: F# Assignment 1 -- Learning Exercises

let rec maxCubeVolume l =
    match l with
    [] -> 0.0
    | (a,b,c)::xs -> let vol = maxCubeVolume xs
                        in
                        if vol > System.Math.a*b*c
                        then a
                        else System.Math.a*b*c;;

/// Testing maxCubeVolume

let r = maxCubeVolume [(2.1, 3.4, 1.8); (4.7, 2.8, 3.2);
                     (0.9, 6.1, 1.0); (3.2, 5.4, 9.9)]);;

printf "%f" r;;
*)
