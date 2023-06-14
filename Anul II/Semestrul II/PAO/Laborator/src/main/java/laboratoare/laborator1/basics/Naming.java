package main.java.laboratoare.laborator1.basics;

/**
 * @author cvoinea
 *
 * This class outlines proper naming of packages, classes, fields, constants and methods.
 *      * https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html
 *
 * Package names are written in all lowercase to avoid conflict with the names of classes or interfaces.
 * Companies use their reversed Internet domain name to begin their package names
 *      (e.g., com.example.mypackage for a package named mypackage created by a programmer at example.com)
 * Therefore, if name collisions occur within a single company, they need to be handled by convention within that company only.
 *      * https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html
 *
 * Class names should be nouns, in mixed case with the first letter of each internal word capitalized. Try to keep your class names simple and descriptive. Use whole words-avoid acronyms and abbreviations
 * Class names should start with an uppercase letter and follow the rest of the rules for any identifier.
 */
public class Naming {

    /**
     * Identifier names (for fields, method, parameters, etc.) can contain letters (both upper and lower case), numbers,
     * the $ sign or _. However, it is recommended that the following rules are respected, for standardisation:
     * - variable names start with lowercase letters.
     * - if variable names contain multiple words, the first one is lowercase and each subsequent word start with only it's
     * first letter as an uppercase.
     */
    private int camelCaseVariableIdentifier;

    /**
     * Constant values are usually named using uppercase letters. If the field name consists of multiple words,
     * use underscore to separate them.
     */
    private final int CONSTANT_VALUE = 3;

    /**
     * Methods should be verbs, in mixed case with the first letter lowercase, with the first letter of each internal word capitalized.
     */
    public void doSomething(){
        // method logic goes here
    }
}
