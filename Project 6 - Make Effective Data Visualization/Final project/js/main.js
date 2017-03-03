
// header
    var Title = d3.select('#title')
                                .append("h2")
                        
                                .text("Survival chances of the Titanic's passangers");
//description 
    var Header = d3.select('#description')
                                .append("h3")
                                .text("RMS Titanic was a British passenger liner that sank in the North Atlantic Ocean in the early morning of 15 April 1912, after colliding with an iceberg during her maiden voyage from Southampton to New York City. Of the 2,224 passengers and crew aboard, more than 1,500 died in the sinking, making it one of the deadliest commercial peacetime maritime disasters in modern history. Passengers and some crew members were evacuated in lifeboats and many of them were launched only partially loaded. There were not enought lifeboats for all the passangers and due to the ocean's temperature it was not possible to survive long time in the water. Below you will find a survivor's breakdown of the Titanic passangers. It will include following data: gender, class, age, port of embarkment. Unfortunatelly only the data of only 891 passengers were available. After the data clean-up of the original dataset (removing passangers that had missing data) 715 passangers remained.")
                                .attr("align","center");
    //description 
    var question = d3.select('#question')
                                .append("h5")
                                .text("Women and children first? Or was every man for himself on a sinking Titanic? See the graphs below.")
                                .attr("align","center");
       
  d3.csv("data/titanic.csv", function (data) {

   /*D3.js setup code*/
    scaler = 0.5
    "use strict";
    var margin = 60,
    width = 800 * scaler,
    height = 600 * scaler;

 
//Chart 1 - Survival by gender (female, male)
    var svg1 = d3.select("#chart1")
              .append("svg")
              .attr("width", width + margin)
              .attr("height", height + margin);

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
                .attr("y", chart._yPixels() - 25)
                 // Align to center
                .style("text-anchor", "middle")
                .style("font-weight", "bold")
                .style("font-family", "sans-serif")
                .text("Survival rate by sex ")

    chart.draw();
    //Change title of y axis
    yAxis.titleShape.text("Number of Passangers");

  //Chart 2 Aduls vs Children

    var svg2 = d3.select("#chart1")
              .append("svg")
              .attr("width", width + margin)
              .attr("height", height + margin);

              var chart = new dimple.chart(svg2, data);
              var xAxis = chart.addCategoryAxis("x", ["Age_Type"]);
              xAxis.addOrderRule(["Adult", "Child"]);
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg2.append("text")
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 50)
                   // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival by age group ")

    chart.draw();
    //Change title of y axis
    yAxis.titleShape.text("Number of Passangers");

    //description graph1
    var Desc1 = d3.select('#description1')
                                .append("h4")
                                .text("Looking at above displayed plots we can clearly observe that more women than men survived. Only about 1/5 of all male passangers survived wheras 3/4 of female managed to save their lifes. Being a child (people below and including 18 years old are considered as children) also turned out have positive infuence on the chances of survival.")
                                .attr("align","center");


    //Chart representing age distribution of the passangers
  
    var svg3 = d3.select("#chart2")
            .append("svg")
            .attr('id','svg3')
            .attr("width", width + margin)
            .attr("height", height + margin);

              var chart = new dimple.chart(svg3, data);
              var xAxis = chart.addCategoryAxis("x", ["Age_Group"]);
              xAxis.addOrderRule(["0-10","11-20", "21-30", "31-40", "41-50", "51-60", "61-70","71-80"])
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg3.append("text")
              // Position in the center of the shape (vertical position is
              // manually set due to cross-browser problems with baseline)
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 25)
                   // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival per Embarked location by sex ")
      chart.draw();
      yAxis.titleShape.text("Procent of Passangers");


    // Upon clicking the button, chart of Class perspective will be created

  d3.select("#btn_1").on("click", function() {
      d3.selectAll("#svg3").remove();

      var svg4 = d3.select("#chart2")
            .append("svg")
            .attr('id','svg3')
            .attr("width", width + margin)
            .attr("height", height + margin);

                var chart = new dimple.chart(svg4, data);
                var xAxis = chart.addCategoryAxis("x", ["Age_Group"]);
                xAxis.addOrderRule(["0-10","11-20", "21-30", "31-40", "41-50", "51-60", "61-70","71-80"])
                var yAxis = chart.addPctAxis("y", "Count");
                var Series = chart.addSeries("Survived", dimple.plot.bar);
                Series.addOrderRule(["Survived","Perished"]);
                var Legend = chart.addLegend(60, 23, 350, 20, "right");
                svg4.append("text")
                // Position in the center of the shape (vertical position is
                // manually set due to cross-browser problems with baseline)
                    .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                    .attr("y", chart._yPixels() - 25)
                     // Align to center
                    .style("text-anchor", "middle")
                    .style("font-weight", "bold")
                    .style("font-family", "sans-serif")
                    .text("Survival per Embarked location by sex ")
        chart.draw();
        yAxis.titleShape.text("Procent of Passangers");
    
    });

    d3.select("#btn_2").on("click", function() {
      d3.selectAll("#svg3").remove();

      var svg4 = d3.select("#chart2")
            .append("svg")
            .attr('id','svg3')
            .attr("width", width + margin)
            .attr("height", height + margin);

                var chart = new dimple.chart(svg4, data);
                var xAxis = chart.addCategoryAxis("x", ["Age_Group"]);
                xAxis.addOrderRule(["0-10","11-20", "21-30", "31-40", "41-50", "51-60", "61-70","71-80"])
                var yAxis = chart.addMeasureAxis("y", "Count");
                var Series = chart.addSeries("Survived", dimple.plot.bar);
                Series.addOrderRule(["Survived","Perished"]);
                var Legend = chart.addLegend(60, 23, 350, 20, "right");
                svg4.append("text")
                // Position in the center of the shape (vertical position is
                // manually set due to cross-browser problems with baseline)
                    .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                    .attr("y", chart._yPixels() - 25)
                     // Align to center
                    .style("text-anchor", "middle")
                    .style("font-weight", "bold")
                    .style("font-family", "sans-serif")
                    .text("Survival per Embarked location by sex ")
      chart.draw();
      yAxis.titleShape.text("Procent of Passangers");


  });

//description2
  var Desc2 = d3.select('#description2')
                                .append("h4")
                                .text("Loolo survival.")
                                .attr("align","center");
                              

//question 
  var question = d3.select('#question2')
                                .append("h5")
                                .text("Rich vs. poor?")
                                .attr("align","center");


//Chart 4: Class versus sex
  var svg4 = d3.select("#chart3")
            .append("svg")
            .attr("width", width + margin)
            .attr("height", height + margin);

              var chart = new dimple.chart(svg4, data);
              var xAxis = chart.addCategoryAxis("x", ["Class", "Class_Sex"]);
              //xAxis.addOrderRule(["First Class Female","First Class Male", "Second Class Female", "Second Class Male", "Third Class Female", "Third Class Male"]);
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg4.append("text")
              // Position in the center of the shape (vertical position is
              // manually set due to cross-browser problems with baseline)
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 25)
                   // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival per Class and ex ")
              chart.draw();
              yAxis.titleShape.text("Number of Passangers");
  });