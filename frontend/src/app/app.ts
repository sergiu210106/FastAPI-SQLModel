import { Component, signal, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Backend } from './services/backend';

@Component({
  selector: 'app-root',
  imports: [CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.css',
  standalone: true,
})
export class App implements OnInit {
  private backend = inject(Backend);
  
  // State as Signals
  data = signal<any>(null);
  error = signal<string | null>(null);
  uploadResponse = signal<any>(null);

  isDragging = false;

  ngOnInit(): void {
    this.backend.getData().subscribe({
      next: (response) => {
        this.data.set(response);
        this.error.set(null);
      },
      error: (err) => {
        this.error.set('Failed to fetch data from the backend.');
        console.error('Error fetching data:', err);
      }
    });
  }

  onFileSelected(event: any): void {
    const file: File = event.target.files[0];
    if (file) {
      this.uploadFile(file);
    }
    event.target.value = ''; 
  }

  onDragOver(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isDragging = true;
  }

  onDragLeave(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isDragging = false;
  }

  onDrop(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isDragging = false;

    if (event.dataTransfer && event.dataTransfer.files.length > 0) {
      const file: File = event.dataTransfer.files[0];
      this.uploadFile(file);
    }
  }

  private uploadFile(file: File): void {
    this.uploadResponse.set(null);
    this.error.set(null);

    this.backend.uploadFile(file).subscribe({
      next: (response) => {
        // Signals ensure the UI updates instantly here
        this.uploadResponse.set(response);
        console.log('Received response from backend:', response); 
      },
      error: (err) => {
        this.error.set('Failed to upload file.');
        console.error(err);
      }
    });
  }
}