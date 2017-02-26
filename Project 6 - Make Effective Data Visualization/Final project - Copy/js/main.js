
// header
    var Title = d3.select('#title')
                                .append("h2")
                        
                                .text("Survival Chance on the Titanic's passange");
//description 
    var Header = d3.select('#description')
                                .append("h3")
                                .text("RMS Titanic was a British passenger liner that sank in the North Atlantic Ocean in the early morning of 15 April 1912, after colliding with an iceberg during her maiden voyage from Southampton to New York City. Of the 2,224 passengers and crew aboard, more than 1,500 died in the sinking, making it one of the deadliest commercial peacetime maritime disasters in modern history. Passengers and some crew members were evacuated in lifeboats and many of them were launched only partially loaded. There were not enought lifeboats for all the passangers and due to the ocean water temperature it was not possible to survive long time in the water. Below you will find a survival breakdown of the Titanic passangers. This will include gender, class, age, port of embarkment. Unfortunatelly only the data of only 891 passengers were available.")
                                .attr("align","center");
       

   /*D3.js setup code*/
    scaler = 0.5
    "use strict";
    var margin = 40,
    width = 800 * scaler,
    height = 600 * scaler;

 
//Chart 1 - Survival by gender (female, male)
    var svg1 = d3.select("#chart1")
              .append("svg")
              .attr("width", width + margin)
              .attr("height", height + margin);

    d3.csv("data/titanic.csv", function (data) {
              var chart = new dimple.chart(svg1, data);
              var xAxis = chart.addCategoryAxis("x", ["Sex"]);
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg1.append("text")
              // Position in the center of the shape (vertical position is
              // manually set due to cross-browser problems with baseline)
                .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                .attr("y", chart._yPixels() - 20)
                 // Align to center
                .style("text-anchor", "middle")
                .style("font-weight", "bold")
                .style("font-family", "sans-serif")
                .text("Survival rate by sex ")

    chart.draw();
    //Change title of y axis
    yAxis.titleShape.text("Number of passangers");
    });

    //Chart 2 - Survival by sex and class;

    var svg2 = d3.select("#chart1")
            .append("svg")
            .attr("width", width + margin)
            .attr("height", height + margin);

    d3.csv("data/titanic.csv", function (data) {
              var chart = new dimple.chart(svg2, data);
              var xAxis = chart.addCategoryAxis("x", ["Age_Type"]);
              xAxis.addOrderRule(["Adult", "Child"]);
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg2.append("text")
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 20)
                   // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival by age group ")

    chart.draw();
    //Change title of y axis
    yAxis.titleShape.text("Number of passangers")
    });


//description graph1
    var Desc1 = d3.select('#description1')
                                .append("h4")
                                .text("We can observed that majority of passangers in third class persihed. ")
                                .attr("align","center");

//graph2
    var svg3 = d3.select("#chart2")
      .append("svg")
      .attr("width", width + margin)
      .attr("height", height + margin);

    d3.csv("data/titanic.csv", function (data) {
                var chart = new dimple.chart(svg3, data);
                var xAxis = chart.addCategoryAxis("x", ["Class","Sex"]);
                xAxis.addOrderRule(["First", "Second", "Third"]);
                var yAxis = chart.addMeasureAxis("y", "Count");
                var Series = chart.addSeries("Survived", dimple.plot.bar);
                Series.addOrderRule(["Survived","Perished"]);
                /*chart.addOrderRule(["Survived","Perished"]);*/
                var Legend = chart.addLegend(60, 23, 350, 20, "right");

                svg3.append("text")
                    .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                    .attr("y", chart._yPixels() - 20)
                     // Align to center
                    .style("text-anchor", "middle")
                    .style("font-weight", "bold")
                    .style("font-family", "sans-serif")
                    .text("Survival by sex per class ")
    chart.draw();
    yAxis.titleShape.text("Number of passangers");
    });

    var svg4 = d3.select("#chart2")
      .append("svg")
      .attr("width", width + margin)
      .attr("height", height + margin);


    d3.csv("data/titanic.csv", function (data) {
              var chart = new dimple.chart(svg4, data);
              var xAxis = chart.addCategoryAxis("x", ["Embarked", "Sex"]);
              var yAxis = chart.addPctAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg4.append("text")
                // Position in the center of the shape (vertical position is
                // manually set due to cross-browser problems with baseline)
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 20)
                   // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival per Embarked location by sex ")
    chart.draw();
    yAxis.titleShape.text("Number of passangers");
    });


//description set of graphs 2
    var Desc2 = d3.select('#description2')
                                .append("h4")
                                .text("We can observed that majority of passangers in third class persihed. ")
                                .attr("align","center");
