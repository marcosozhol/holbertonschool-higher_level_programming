#!/usr/bin/node

exports.nbOccurences = function (list, searchelement) {
    return (list.filter(elem => elem === searchelement).length)
};