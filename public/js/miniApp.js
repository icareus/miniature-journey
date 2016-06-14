var app = angular.module('miniApp', []);

app.factory('pics', [function(){
    var o = {
        pics: [
            new pic('Untitled picture', 'Look sis, I\'m trying!'),
        ]
    };
    return o;
}])

app.factory('sections', [function(){
	var o = {
		sections: [
			new section("about", "Qui suis-je ?", [
					`Blabla j'aime faire des jolies photos, et mon grand frere m'a fait un super sitepour faire decouvrir mes talents dans cette discipline. Au final tout ceci n'est que du texte de remplissage, ca se voit bien !`,
					`En attendant de les remplacer par les tiennes, les photos viennent de gratisography.com et la carte utilise snazzymaps.com.`,
					`Blablabla cette ligne parlait de tout le bordel superflu livre avec le theme`,
				]),
			new section("download", "Photographie", [
					`On fera des trucs ici aussi`,
					`Genre mettre des trucs styles, des photos et tout`,
				]),
			new section("contact", "Contactez-moi =)", [
					`Le site etant encore en consctruction j'ai la flemme de mettre ce formulaire de contact`,
					`En attendant, un contact broken`,
				]),
		]
	};
	return o;
}])

var pic = function(title, description, src="/uploads/placeholder"){
    this.title = title;
    this.description = description;
    this.src = src;
}

var section = function(title, nav, content = []){
    this.title = title;
    this.nav = nav;
    this.content = content;
}

app.controller('mainCtrl', [
    '$scope',
    'pics',
    'sections',
    function($scope, pics, sections){
    	$scope.sections = sections.sections;
        $scope.pics = pics.pics;
    }]);