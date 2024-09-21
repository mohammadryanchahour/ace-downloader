from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, QRectF, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor

class ProgressTrackerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.percentage = 0  # Track the percentage of completion
        self.speed = 0        # Download speed in KB/s
        self.setMinimumSize(200, 200)

        # Labels for percentage and speed display
        self.label_percentage = QLabel(f"{self.percentage}%", self)
        self.label_percentage.setAlignment(Qt.AlignCenter)
        self.label_speed = QLabel(f"Speed: {self.speed} KB/s", self)
        self.label_speed.setAlignment(Qt.AlignCenter)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_percentage)
        layout.addWidget(self.label_speed)
        self.setLayout(layout)

        # Redraw the widget every second (for progress update simulation)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def update_progress(self, percentage, speed):
        """Update the percentage and speed"""
        self.percentage = percentage
        self.speed = speed
        self.label_percentage.setText(f"{self.percentage}%")
        self.label_speed.setText(f"Speed: {self.speed} KB/s")
        self.update()

    def paintEvent(self, event):
        """Override to draw the circular progress"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Set up pen for drawing progress circle
        pen = QPen(QColor(100, 150, 200), 10)  # Customizable color
        painter.setPen(pen)

        # Define the size and position for the circle
        rect = QRectF(10, 10, self.width() - 20, self.height() - 20)
        start_angle = 90 * 16  # Start at the top of the circle
        span_angle = -self.percentage * 3.6 * 16  # Negative for clockwise
        
        # Draw circular arc based on percentage
        painter.drawArc(rect, start_angle, span_angle)
