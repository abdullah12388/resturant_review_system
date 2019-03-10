
var app = angular.module('app', []);
app.config(function($httpProvider) {
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
app.controller('ctrl', function($scope, $http){
	$scope.restaurants = '';
	var userKey = 'cd9ca69cad612fbd6b4cb9fe9d503906';
	var search_url = 'https://developers.zomato.com/api/v2.1/search?entity_id=4&entity_type=city&count=10'
	$scope.query_string = '';
	$scope.queryStringParams = {};

	$scope.fetchRestaurants = function (query) {
		debugger;
		if(query !== undefined){
			search_url = search_url+"&q="+query;
		}
		if('cuisines' in $scope.queryStringParams){
			search_url = search_url+"&cuisines="+$scope.queryStringParams.cuisines;
		}
		if('category' in $scope.queryStringParams){
			search_url = search_url+"&category="+$scope.queryStringParams.category;
		}
		if('establishments' in $scope.queryStringParams){
			search_url = search_url+"&establishment_type="+$scope.queryStringParams.establishments;
		}
		$http({
		method: 'GET',
		url: search_url,
		headers: {
			'Content-Type':  'application/json',
			'user-key': userKey
		}
		}).then(
		function successCallback(response) {
			$scope.restaurants = response.data.restaurants;
			console.log(response.data);
		}, function errorCallback(response) {
			    alert("some thing went wrong please try again");
			});

	};
	
	//initial call
	$scope.fetchRestaurants();

	$scope.categories = [];
	$scope.fetchData = function (category_string) {
		delete $scope.queryStringParams.category;
		$http({
			headers: {
				'Accept': 'application/json',
				'user-key': userKey
			},
			method: "GET",
			url: "https://developers.zomato.com/api/v2.1/categories",
		}).then(
		function successCallback(response) {
			$scope.categories = response.data.categories;
			var output=[];
			angular.forEach($scope.categories,function(category){
				if(category.categories.name.toLowerCase().indexOf(category_string.toLowerCase())>=0){
					output.push(category.categories);
				}
			});
			$scope.resultData=output;
		},
		function errorCallback(response) {
			alert("some thing went wrong please try again");
		})
	};

	$scope.cuisines = [];
	$scope.fetchCusine = function (cusine_string, param) {
		delete $scope.queryStringParams.cuisines;
		$http({
			headers: {
				'Accept': 'application/json',
				'user-key': userKey
			},
			method: "GET",
			url: "https://developers.zomato.com/api/v2.1/"+param+"?city_id=4",
		}).then(
		function successCallback(response) {
			$scope.cuisines = response.data.cuisines;
			var output=[];
			angular.forEach($scope.cuisines,function(list){
				if(list.cuisine.cuisine_name.toLowerCase().indexOf(cusine_string.toLowerCase())>=0){
					output.push(list.cuisine);
				}
			});
			$scope.cuisineResult=output;
		},
		function errorCallback(response) {
			alert("some thing went wrong please try again");
		})
	};

	$scope.types = [];
	$scope.fetchType = function (type_string, param) {
		delete $scope.queryStringParams.establishments;
		$http({
			headers: {
				'Accept': 'application/json',
				'user-key': userKey
			},
			method: "GET",
			url: "https://developers.zomato.com/api/v2.1/"+param+"?city_id=4",
		}).then(
		function successCallback(response) {
			$scope.types = response.data.establishments;
			var output=[];
			angular.forEach($scope.types,function(list){
				if(list.establishment.name.toLowerCase().indexOf(type_string.toLowerCase())>=0){
					output.push(list.establishment);
				}
			});
			$scope.typeResult=output;
		},
		function errorCallback(response) {
			alert("some thing went wrong please try again");
		})
	};

	
	$scope.fillTextbox=function(object, parameter){
		switch (parameter){
			case 'category' :
				$scope.queryStringParams.category = object.id;
				$scope.search_category = object.name;
				$scope.resultData=null;
				break;
			case 'cuisines' :
				$scope.queryStringParams.cuisines = object.cuisine_id;
				$scope.search_cuisine = object.cuisine_name;
				$scope.cuisineResult=null;
				break;
			case 'establishments' :
				$scope.queryStringParams.establishments = object.id;
				$scope.search_type = object.name;
				$scope.typeResult=null;
				break;
			default :
				break;
		}
		console.log($scope.queryStringParams);
	}
});

