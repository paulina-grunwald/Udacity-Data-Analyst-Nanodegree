
// header
    var Title = d3.select('#title')
                                .append("h2")
                                .text("Survival chances of the Titanic's passangers");
//description 
    var Header = d3.select('#description')
                                .append("h3")
                                .text("RMS Titanic was a British passenger liner that sank in the North Atlantic Ocean in the early morning of 15 April 1912, after colliding with an iceberg during her maiden voyage from Southampton to New York City. Of the 2,224 passengers and crew aboard, more than 1,500 died in the sinking, making it one of the deadliest commercial peacetime maritime disasters in modern history. Passengers and some crew members were evacuated in lifeboats and many of them were launched only partially loaded. There were not enough lifeboats for all the passengers and due to the ocean's temperature it was not possible to survive long time in the water. Below you will find a survivor's breakdown of the Titanic passengers. It will include following data: gender, class, age, port of embankment. Unfortunately only the data of only 891 passengers were available. After the data clean-up of the original dataset (removing passengers that had missing data) 715 passengers remained.")
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
              chart.assignColor("Perished", "rgb(217,95,2)");
              chart.assignColor("Survived", "rgb(27,158,119)");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg1.append("text")
              // Position in the center of the shape 
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
              chart.assignColor("Perished", "rgb(217,95,2)");
              chart.assignColor("Survived", "rgb(27,158,119)");
              xAxis.title = 'Age group'
              xAxis.addOrderRule(["Adult", "Child"]);
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg2.append("text")
                  // Position in the center of the shape 
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 25)
                  // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival rate by age group")

      chart.draw();
      //Change title of y axis
      yAxis.titleShape.text("Number of Passangers");

      //description graph1
      var Desc1 = d3.select('#description1')
              .append("h4")
              .text("Looking at above displayed plots we can clearly observe that more women than men survived. Only about 1/5 of all male passengers survived whereas 3/4 of female managed to save their life. Being a child (in my investigation people below and including 18 years old are considered as children) also turned out have positive influence on the chances of survival. Let's have a look at survival rate in various age groups. Click on percent and count buttons to change y Axis display.")
              .attr("align","center");


      //Chart representing age distribution of the passangers
  
      var svg3 = d3.select("#chart2")
              .append("svg")
              .attr('id','svg3')
              .attr("width", width + margin+80)
              .attr("height", height + margin);

              var chart = new dimple.chart(svg3, data);
              var xAxis = chart.addCategoryAxis("x", ["Age_Group"]);
              xAxis.title = 'Age group'
              chart.assignColor("Perished", "rgb(217,95,2)");
              chart.assignColor("Survived", "rgb(27,158,119)");
              xAxis.addOrderRule(["0-10","11-20", "21-30", "31-40", "41-50", "51-60", "61-70","71-80"])
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg3.append("text")
                  // Position in the center of the shape
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 25)
                  // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival rate by age group")
      chart.draw();
      yAxis.titleShape.text("Percent of Passangers");


    // Upon clicking the button, chart of Class perspective will be created

      d3.select("#btn_procent").on("click", function() {
          d3.selectAll("#svg3").remove();

          var svg4 = d3.select("#chart2")
              .append("svg")
              .attr('id','svg3')
              .attr("width", width + margin+80)
              .attr("height", height + margin);

              var chart = new dimple.chart(svg4, data);
              var xAxis = chart.addCategoryAxis("x", ["Age_Group"]);
              chart.assignColor("Perished", "rgb(217,95,2)");
              chart.assignColor("Survived", "rgb(27,158,119)");
              xAxis.title = 'Age group'
              xAxis.addOrderRule(["0-10","11-20", "21-30", "31-40", "41-50", "51-60", "61-70","71-80"])
              var yAxis = chart.addPctAxis("y", "Count");
              yAxis.title = 'Percent of Passangers'
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg4.append("text")
                  // Position in the center of the shape 
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 25)
                  // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival rate by age group")
          chart.draw();
       
    
      });

      d3.select("#btn_count").on("click", function() {
          d3.selectAll("#svg3").remove();

          var svg4 = d3.select("#chart2")
              .append("svg")
              .attr('id','svg3')
              .attr("width", width + margin+80)
              .attr("height", height + margin);

              var chart = new dimple.chart(svg4, data);
              var xAxis = chart.addCategoryAxis("x", ["Age_Group"]);
              chart.assignColor("Perished", "rgb(217,95,2)");
              chart.assignColor("Survived", "rgb(27,158,119)");
              xAxis.addOrderRule(["0-10","11-20", "21-30", "31-40", "41-50", "51-60", "61-70","71-80"])
              xAxis.title = 'Age group'
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              var Legend = chart.addLegend(60, 23, 350, 20, "right");
              svg4.append("text")
                  // Position in the center of the shape 
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 25)
                  // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival rate by group")
      chart.draw();
      yAxis.titleShape.text("Number of Passangers");

      });

    //description2
    var Desc2 = d3.select('#description2')
            .append("h4")
            .text("Having closer look at the survived versus perished passengers in various age group we can conclude that the passengers from age 0 to 10 had the biggest chance of survival. The passengers in age group 61 to 80 had the lowest chance of survival.")
            .attr("align","center");
                              

    //question 
    var question = d3.select('#question2')
            .append("h5")
            .text("Did rich people had better chances of survival?")
            .attr("align","center");


    //Chart 4: Class versus sex
    var svg4 = d3.select("#chart3")
            .append("svg")
            .attr("width", width + margin)
            .attr("height", height + margin);

            var chart = new dimple.chart(svg4, data);
            var xAxis = chart.addCategoryAxis("x", ["Class"]);
            xAxis.addOrderRule(["First","Second", "Third"]);
            chart.assignColor("Perished", "rgb(217,95,2)");
            chart.assignColor("Survived", "rgb(27,158,119)");
            var yAxis = chart.addMeasureAxis("y", "Count");
            var Series = chart.addSeries("Survived", dimple.plot.bar);
            Series.addOrderRule(["Survived","Perished"]);
            var Legend = chart.addLegend(60, 23, 350, 20, "right");
            svg4.append("text")
              // Position in the center of the shape 
                .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                .attr("y", chart._yPixels() - 25)
                // Align to center
                .style("text-anchor", "middle")
                .style("font-weight", "bold")
                .style("font-family", "sans-serif")
                .text("Survival rate by class")
    chart.draw();
    yAxis.titleShape.text("Number of Passangers");


    var svg5 = d3.select("#chart3")
            .append("svg")
            .attr("width", width + margin)
            .attr("height", height + margin);

            var chart = new dimple.chart(svg5, data);
            var xAxis = chart.addCategoryAxis("x", ["Class","Sex"]);
            xAxis.title = 'Class and Sex'
            chart.assignColor("Perished", "rgb(217,95,2)");
            chart.assignColor("Survived", "rgb(27,158,119)");
            xAxis.addOrderRule(["First", "Second", "Third"])
            var yAxis = chart.addMeasureAxis("y", "Count");
            var Series = chart.addSeries("Survived", dimple.plot.bar);
            Series.addOrderRule(["Survived","Perished"]);
            var Legend = chart.addLegend(60, 23, 350, 20, "right");
            svg5.append("text")
              // Position in the center of the shape 
                  .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                  .attr("y", chart._yPixels() - 50)
                   // Align to center
                  .style("text-anchor", "middle")
                  .style("font-weight", "bold")
                  .style("font-family", "sans-serif")
                  .text("Survival by Class and Sex")
    chart.draw();
    yAxis.titleShape.text("Number of Passangers");

    var Desc3 = d3.select("#description3")
                                .append("h6")
                                .text("Titanic's passengers were separated in three classes. The Titanic's first-class passengers were rich and prominent members of the upper class. Titanic second class passengers were leisure tourists, academics, members of the clergy and middle class English and American families. The third class consisted of rather poor passengers who left their countries in hope of starting new life in the United States. Third class and crew cabins were located in the hold, while promenade areas were on lower decks and in the quarter. They were separated from the promenade decks for wealthier passengers by special partitions – staircases leading to upper decks had metal gates. They key to the gates was kept by the vessel crew. Some sources claim that these partitions were required by American immigration laws at the time. The majority of passengers on the Titanic were emigrants. It Only 25 percent of the Titanic’s third class passengers survived. On the other hand we can observe high survival rate in the passengers in the first class. According to many sources they had easier access to the life boats. In general men (regardless in which class there were placed) had bigger chance of loosing their life in comparison to woman. We have to remember though that much bigger percent of men from 3rd class perished in comparison to the first class.")
                                .attr("align","enter");
    });