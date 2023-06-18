library(shiny)
library(ggplot2)


# FRONTEND
ui <- fluidPage(
  titlePanel("Chaos Game Project"),
  
  sidebarLayout(
    
    # Inputuri
    sidebarPanel(
      selectInput("shape", "Shape:",
                  c("Triangle" = "triangle",
                    "Pentagon" = "pentagon",
                    "Hexagon" = "hexagon")),
      numericInput("iterations", "Iterations:", value = 1000, min = 1000, max = 25000, step = 1000),
      sliderInput("ratio", "Chaos Ratio:", min = 0.05, max = 0.95, value=0.5, round = FALSE, step = 0.05),
      
      actionButton("reload", "Reload")
    ),
    
    mainPanel(
      plotOutput("plot", width = "500px", height = "500px")
    )
  )
)



# BACKEND
server <- function(input, output) {
  chaos_game <- function(shape, iterations, ratio) {
    if (shape == "triangle") {
      vertices <- matrix(c(-0.75, -0.75,
                           0.75, -0.75,
                           0, 0.75),
                         ncol = 2, byrow = TRUE)
    } 
    else if (shape == "pentagon") {
      vertices <- matrix(c(sin(pi/5), cos(pi/5),
                           sin(3*pi/5), cos(3*pi/5),
                           sin(5*pi/5), cos(5*pi/5),
                           sin(7*pi/5), cos(7*pi/5),
                           sin(9*pi/5), cos(9*pi/5)),
                         ncol = 2, byrow = TRUE)
    }
    else if (shape == "hexagon") {
      vertices <- matrix(c(sin(pi/6), cos(pi/6),
                           sin(3*pi/6), cos(3*pi/6),
                           sin(5*pi/6), cos(5*pi/6),
                           sin(7*pi/6), cos(7*pi/6),
                           sin(9*pi/6), cos(9*pi/6),
                           sin(11*pi/6), cos(11*pi/6)),
                         ncol = 2, byrow = TRUE)
    }
    
    x <- c(0)
    y <- c(0)

   for (i in 1:iterations) {
     vertex <- sample(1:nrow(vertices), 1)
     x[i+1] <- (x[i] + vertices[vertex, 1]) * ratio
     y[i+1] <- (y[i] + vertices[vertex, 2]) * ratio
    }

    return(data.frame(x = x, y = y))
  }
  
  observeEvent(input$reload, {
    req(input$shape, input$iterations, input$ratio)
    output$plot <- renderPlot({
      points <- chaos_game(input$shape, input$iterations, input$ratio)
      ggplot(points, aes(x = x, y = y)) +
        geom_point() +
        xlim(-1, 1) +
        ylim(-1, 1)
    })
  })
}

shinyApp(ui = ui, server = server)